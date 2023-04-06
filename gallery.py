#!/usr/bin/env python3
import os
import re
import sys
import time
import json
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from multiprocessing.pool import ThreadPool

requests_proxy = {
        # 'https': 'socks5://127.0.0.1:1080',
        }

requests_headers = {
        'User-Agent': "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0",
        }

filename_filter = {
        47: 45,
        34: '',
        }

SLEEP_TIME = 0.6


def download_image(img_url, img_name=None):
    global SLEEP_TIME
    if img_url is None:
        return None
    time.sleep(SLEEP_TIME)
    while True:
        try:
            response = requests.get(img_url, headers=requests_headers, stream=True, proxies=requests_proxy)
        except Exception as e:
            print("error saving image: " + str(img_url), file=sys.stderr)
            print(e, file=sys.stderr)
            time.sleep(180)
            SLEEP_TIME += 0.2
        else:
            if response.status_code == 200:
                if img_name is None:
                    try:
                        d = response.headers['content-disposition']
                        img_name = re.findall("filename=(.+)", d)[0].translate(filename_filter)
                    except Exception as e:
                        print(e, file=sys.stderr)
                        img_name = str(int(time.time()))
                if not os.path.exists(img_name):
                    with open(img_name, 'wb') as file:
                        for chunk in response.iter_content(1048576):
                            file.write(chunk)
                return os.path.splitext(img_name)[0]
            elif response.status_code == 404:
                print("image net found: " + str(img_url), file=sys.stderr)
                return None
            else:
                print("error saving image: " + str(img_url), file=sys.stderr)
                print(response.status_code, file=sys.stderr)
                print(response.text, file=sys.stderr)
                time.sleep(180)
                SLEEP_TIME += 0.2


def save_image(img_info):
    time.sleep(SLEEP_TIME)
    base_name = download_image(img_info['rawUrl'])
    if base_name is None:
        base_name = img_info['id']
    download_image(img_info['url'], base_name + '.jpg')
    with open(base_name + '.json', 'w') as file:
        file.write(str(img_info))


def get_gallery(id):
    global SLEEP_TIME
    time.sleep(SLEEP_TIME)
    url = f"https://www.dpreview.com/sample-galleries/data/get-gallery?galleryId={id}&isMobile=false"
    while True:
        try:
            response = requests.get(url, headers=requests_headers, proxies=requests_proxy)
        except Exception as e:
            print(e)
            print(url)
            time.sleep(180)
            SLEEP_TIME += 0.2
            continue
        try:
            res = response.json()
            return res
        except Exception as e:
            print(e)
            print(response.status_code)
            print(response.text)
            if response.status_code != 404:
                time.sleep(180)
                SLEEP_TIME += 0.2
            else:
                return {}


def get_galleries_list():
    url = "https://www.dpreview.com/sample-galleries"
    response = requests.get(url, headers=requests_headers, proxies=requests_proxy)
    soup = BeautifulSoup(response.text, "html.parser")
    galleries = soup.select('tr.gallery')
    return [json.loads(g['data-gallery'])['id'] for g in galleries]


if __name__ == "__main__":
    for gid in get_galleries_list():
        gallery_info = get_gallery(gid)
        if 'gallery' not in gallery_info:
            continue

        print("fetching", gallery_info['gallery']['title'])

        save_path = str(gid) + ". " + gallery_info['gallery']['title'].translate(filename_filter)
        olddir = os.getcwd()
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        os.chdir(save_path)

        for img in gallery_info['images']:
            save_image(img)

        os.chdir(olddir)

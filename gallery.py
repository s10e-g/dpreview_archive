#!/usr/bin/env python3
import os
import re
import json
import time
import requests
from bs4 import BeautifulSoup
from urllib.parse import urlparse, unquote

SLEEP_TIME = 0.6


def create_session(user_agent, proxy):
    session = requests.Session()
    session.headers.update({'User-Agent': user_agent})
    session.proxies.update({'http': proxy, 'https': proxy})
    return session


def get_gallery_ids(session, url):
    response = session.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    gallery_elements = soup.find_all('tr', class_='gallery')
    gallery_ids = [json.loads(element['data-gallery'])['id'] for element in gallery_elements]
    return gallery_ids


def get_gallery_info(session, gallery_id):
    global SLEEP_TIME
    time.sleep(SLEEP_TIME)
    url = f"https://www.dpreview.com/sample-galleries/data/get-gallery?galleryId={gallery_id}&isMobile=false"
    while True:
        try:
            response = session.get(url)
            response.raise_for_status()
            return response.json()
        except requests.exceptions.HTTPError as e:
            if e.response.status_code == 429:
                print(f"Gallery ID {gallery_id} got error 429, retry in 180s...")
                SLEEP_TIME += 0.2
                time.sleep(180)
            elif e.response.status_code == 404:
                print(f"Gallery ID {gallery_id} not found, skipping.")
                return None
            else:
                print(f"Error {e.response.status_code}: Unable to get gallery info for ID {gallery_id}.")
                return None


def download_image(session, url, save_path, delay, response=None):
    if os.path.exists(save_path):
        return

    if response is None:
        time.sleep(delay)
        response = session.get(url, stream=True)

    response.raise_for_status()

    with open(save_path, 'wb') as image_file:
        for chunk in response.iter_content(chunk_size=1048576):
            image_file.write(chunk)


def main():
    global SLEEP_TIME
    user_agent = "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/111.0"
    proxy = "socks5://127.0.0.1:1081"
    session = create_session(user_agent, proxy)

    base_url = "https://www.dpreview.com/sample-galleries"
    gallery_ids = get_gallery_ids(session, base_url)

    for gallery_id in gallery_ids[214:700]:
        gallery_info = get_gallery_info(session, gallery_id)

        if gallery_info is None:
            continue

        gallery_title = gallery_info['gallery']['title'].replace('/', '_')
        directory_name = f"{gallery_id}. {gallery_title}"
        print("fetching", gallery_info['gallery']['title'])

        if not os.path.exists(directory_name):
            os.makedirs(directory_name)

        for i in range(len(gallery_info['images'])):
            image = gallery_info['images'][i]
            raw_url = image['rawUrl']
            image_url = image['url']
            image_filename = None

            if raw_url:
                while True:
                    time.sleep(SLEEP_TIME)
                    try:
                        with session.get(raw_url, stream=True) as response:
                            content_disposition = response.headers.get('content-disposition')
                            if content_disposition:
                                raw_filename = re.findall('filename="(.+)"', content_disposition)[0]
                            else:
                                raw_filename = unquote(urlparse(raw_url).path.split('/')[-1])

                            raw_save_path = os.path.join(directory_name, raw_filename)
                            download_image(session, raw_url, raw_save_path, SLEEP_TIME, response)

                            # Handle image_url with the same basename but different extension
                            image_filename = os.path.splitext(raw_filename)[0] + os.path.splitext(urlparse(image_url).path)[-1]
                        break
                    except requests.exceptions.HTTPError as e:
                        if e.response.status_code == 403:
                            print(f"Error {e.response.status_code}: access denied downloading {raw_url} for gallery ID {gallery_id}. Retrying...")
                            gallery_info = get_gallery_info(session, gallery_id)
                            raw_url = gallery_info['images'][i]['rawUrl']
                            image_url = gallery_info['images'][i]['url']
                        elif e.response.status_code == 429:
                            SLEEP_TIME += 0.2
                            time.sleep(180)
                            print(f"Error {e.response.status_code}: {raw_url} for gallery ID {gallery_id}. Retrying...")
                        else:
                            print(f"Error {e.response.status_code}: Unable to download raw image {raw_url} for gallery ID {gallery_id}.")
                            break

            while True:
                if image_filename is None:
                    image_filename = unquote(urlparse(image_url).path.split('/')[-1])
                image_save_path = os.path.join(directory_name, image_filename)
                try:
                    download_image(session, image_url, image_save_path, SLEEP_TIME)
                    break
                except requests.exceptions.HTTPError as e:
                    if e.response.status_code == 403:
                        print(f"Error {e.response.status_code}: access denied downloading {image_filename} for gallery ID {gallery_id}. Retrying...")
                        gallery_info = get_gallery_info(session, gallery_id)
                        image_url = gallery_info['images'][i]['url']
                    elif e.response.status_code == 429:
                        SLEEP_TIME += 0.2
                        time.sleep(180)
                        print(f"Error {e.response.status_code}: {image_filename} for gallery ID {gallery_id}. Retrying...")
                    else:
                        print(f"Error {e.response.status_code}: Unable to download image {image_filename} for gallery ID {gallery_id}.")

            info_path = os.path.join(directory_name, os.path.splitext(image_filename)[0] + '.json')
            if not os.path.exists(info_path):
                with open(info_path, 'w') as file:
                    file.write(str(image))


if __name__ == "__main__":
    main()

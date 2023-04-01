#!/usr/bin/env python3
import os
import sys
import time
import json
import requests
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
        }

SLEEP_TIME = 0.6


def download_image(img_url, img_name):
    if img_url[-1] == '=':
        return

    img_name += os.path.splitext(img_url)[1]
    if os.path.exists(img_name):
        print("skip", img_name)
        return

    # print("processing", img_name)
    try:
        response = requests.get(img_url, headers=requests_headers, stream=True, proxies=requests_proxy)
    except requests.exceptions.RequestException as e:
        print("error saving image: " + str(img_url), file=sys.stderr)
        print(e, file=sys.stderr)
    else:
        if response.status_code == 200:
            with open(img_name, 'wb') as file:
                for chunk in response.iter_content(1048576):
                    file.write(chunk)
        else:
            print("error saving image: " + str(img_url), file=sys.stderr)
            print(response.status_code, file=sys.stderr)
            print(response.text, file=sys.stderr)


def get_images(data):
    global SLEEP_TIME
    url = "https://www.dpreview.com/reviews/image-comparison/get-images"
    requests_data = {
            'data': json.dumps(data)
            }
    while True:
        try:
            response = requests.post(url, headers=requests_headers, data=requests_data, proxies=requests_proxy)
        except Exception as e:
            print(e)
            print(data)
            time.sleep(180)
            continue
        try:
            res = response.json()
            return res
        except Exception as e:
            print("error get_images", e)
            print(data)
            print(response.status_code)
            print(response.text)
            if response.status_code != 404:
                time.sleep(180)
                SLEEP_TIME += 0.2


def image_process_attributes(data, attributes, num_processed=0):
    time.sleep(SLEEP_TIME)
    if not attributes:
        base_name = ''.join([str(i['value'])+'_' for i in data['attributes']])
        base_name = base_name.translate(filename_filter)
        image_info = get_images(data)
        # with open(base_name + str('request'), 'w') as file:
        #     file.write(str(json.dumps(data)))
        # with open(base_name + str('response'), 'w') as file:
        #     file.write(str(image_info))

        for img in image_info['images']:
            img_name = base_name + str(img['id'])
            with open(img_name + '.txt', 'w') as file:
                file.write(str(img['infoText']))

            img_url = urljoin("https://www.dpreview.com/", img['originalUrl'])
            download_image(img_url, img_name)
            print(img_url)

            if img['originalUrl'] != img['displayImageUrl']:
                img_url = urljoin("https://www.dpreview.com/", img['displayImageUrl'])
                download_image(img_url, img_name)
                print(img_url)
        return

    for attr in attributes:
        value = attr['slotValues']['0'] if len(attr['slotValues']) > 0 else None
        data['attributes'].append({
            'instanceId': attr['instanceId'],
            'value': value,
            'isSet': value is not None,
            'allowDefaultUnset': False,
            'isFixed': False,
            })
    res = get_images(data)
    for attr in attributes:
        data['attributes'].pop()

    try:
        legal_values = set(i['clientValue'] for i in res['attributes'][num_processed]['values'])
    except TypeError:
        legal_values = [None]
    except IndexError:
        print('IndexError')
        print('attributes', res['attributes'])
        print('num_processed', num_processed)
        legal_values = [None]

    for value in legal_values:
        data['attributes'].append({
            'instanceId': attributes[0]['instanceId'],
            'value': value,
            'isSet': value is not None,
            'allowDefaultUnset': False,
            'isFixed': False,
            })
        image_process_attributes(data, attributes[1:], num_processed+1)
        data['attributes'].pop()


def get_all_image(widget):
    data = {
            'sceneId': widget['sceneId'],
            'includeImages': True,
            'attributes': list()
            }
    image_process_attributes(data=data, attributes=widget['attributes'])


def get_widget(id):
    global SLEEP_TIME
    url = "https://www.dpreview.com/reviews/image-comparison/get-widget"
    data = {'widget': str(id)}
    while True:
        try:
            response = requests.post(url, headers=requests_headers, data=data, proxies=requests_proxy)
        except Exception as e:
            print(e)
            print(data)
            time.sleep(180)
            continue
        try:
            res = response.json()
            return res
        except Exception as e:
            print(e)
            print(response.status_code)
            print(data)
            print(response.text)
            if response.status_code != 404:
                time.sleep(180)
                SLEEP_TIME += 0.2
            else:
                return {}


if __name__ == "__main__":
    scene_archived = set()
    # for widget_id in range(1, 900):
    for widget_id in [1, 67, 197, 205]:
        widget_info = get_widget(widget_id)
        if 'sceneTitle' not in widget_info:
            continue
        if widget_info['sceneId'] in scene_archived:
            continue

        print("fetching", widget_info['sceneTitle'])

        save_path = str(widget_id) + ". " + widget_info['sceneTitle'].translate(filename_filter)
        olddir = os.getcwd()
        if not os.path.exists(save_path):
            os.makedirs(save_path)
        os.chdir(save_path)

        get_all_image(widget_info)

        os.chdir(olddir)

        scene_archived.add(widget_info['sceneId'])

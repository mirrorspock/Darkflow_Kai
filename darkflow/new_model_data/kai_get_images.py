import json
import os
import random
import requests
import urllib.request as ulib
import urllib.error
from bs4 import BeautifulSoup as bs



url_base = "https://www.google.com/search?q={}&source=lnms&tbm=isch&sa=X&ved=0ahUKEwit38zSwJXcAhWBwVkKHfeqB_gQ_AUICigB&biw=1366&bih=662"


ua = [
'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36',
]

def get_links(search_name):
    search_name = search_name.replace(' ', '+')
    url = url_base.format(search_name, 0)
    cabecera = {"User-Agent": random.choice(ua)}
    req = requests.get(url, headers=cabecera )
    html = req.content
    soup = bs(html,"lxml")
    images = soup.find_all('div', {"class": 'rg_meta notranslate'})
    images = [i.text for i in images]
    images = [json.loads(i) for i in images]
    images = [images['ou'] for images in images]
    return images

def save_images(links, search_name):
    directory = search_name.replace(' ', '_')
    if not os.path.isdir(directory):
        os.mkdir(directory)

    for i, link in enumerate(links):
        print(link)
        savepath = os.path.join(directory, '{:06}.png'.format(i))
        try:
            ulib.urlretrieve(link, savepath)
        except urllib.error.HTTPError as e:
            if e.code in (..., 403, ...):
                print("403")
                continue
        except urllib.error.URLError as e:
            print("URLError")
            continue



if __name__ == '__main__':
    search_name = 'nick wilde drawing'
    links = get_links(search_name)

    # for link in links:
    # 	print(link)
    save_images(links, search_name)
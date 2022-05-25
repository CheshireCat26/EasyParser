from time import sleep

import requests
from bs4 import BeautifulSoup as bs


def get_posts(url):
    r = requests.get(url)
    soup = bs(r.text, "html.parser")
    header_list = soup.find_all('h3', class_='_eYtD2XCVieq6emjKBH3m')
    comments_list = soup.find_all('a', class_="_1UoeAeSRhOKSNdY_h3iS1O _1Hw7tY9pMr-T1F4P1C-xNU _3U_7i38RDPV5eBv7m4M-9J "
                                          "_2qww3J5KKzsD7e5DO0BvvU")

    r_list = []
    if len(header_list) != 0 and len(comments_list) != 0:
        r_list = []
        for h, l in zip(header_list, comments_list):
            r_list.append({'header': h.text, '# comments': l.text})

    return r_list


URL_TEMPLATE = "https://www.reddit.com/r/all/"

posts_list = []
while len(posts_list) == 0:
    posts_list = get_posts(URL_TEMPLATE)
    sleep(5)

for i in posts_list:
    print(i)

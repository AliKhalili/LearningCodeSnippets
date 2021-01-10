import collections

import requests

# BASE_URL = 'https://jamejamonline.ir/fa/news/{id}'
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/39.0.2171.95 Safari/537.36'}
#
# url = BASE_URL.format(id=1299039)
# print(url)
# resp = requests.get(BASE_URL.format(id=1299039), verify=False, headers=headers)
# with open('test.txt', 'w', encoding="utf-8") as f:
#     f.write(resp.text)


from bs4 import BeautifulSoup

html_content = ''
with open('test.txt', encoding='utf-8') as f:
    html_content = f.read()

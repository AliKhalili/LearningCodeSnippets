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


class HtmlField:
    def __init__(self, *, name, selector, **attrs):
        self._name = name
        self._selector = selector
        self._attrs = attrs

    @property
    def name(self):
        return self._name

    @property
    def selector(self):
        return self._selector


class HtmlParser:
    def __init__(self, html_content: str):
        self._soup = BeautifulSoup(html_content, 'html.parser')
        self.fields = {}

    def add_field(self, *, field_name: str, css_selector: str, is_multi: bool = False):
        self.fields[field_name] = HtmlField(name=field_name, selector=css_selector, is_multi=is_multi)

    def parse(self):
        result = {}
        for field_name, field in self.fields.items():
            result[field.name] = self._parse_field(field.name)
        return result

    def _parse_field(self, field_name):
        try:
            text = "NAN"
            filed = self.fields[field_name]
            text = self._soup.select_one(filed.selector).text
        except KeyError as key_error:
            print(key_error)
        except Exception as error:
            print(error)
        return text


html_parser = HtmlParser(html_content)
html_parser.add_field(field_name='post_title', css_selector='div.newstitle > h1.title')
html_parser.add_field(field_name='post_subtitle', css_selector='div.newstitle > h4.rutitr')
html_parser.add_field(field_name='post_content', css_selector='section.newsPageContent')
html_parser.add_field(field_name='post_subtitle', css_selector='div.newstitle > h4.rutitr')
html_parser.add_field(field_name='post_subtitle', css_selector='div.newstitle > h4.rutitr')
result = html_parser.parse()
print(result)

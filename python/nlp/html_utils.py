from bs4 import BeautifulSoup


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


class HmashahriParser(HtmlParser):
    def __init__(self):
        super(HmashahriParser, self).__init__()
        super().add_field(field_name='post_title', css_selector='div.newstitle > h1.title')
        super().add_field(field_name='post_subtitle', css_selector='div.newstitle > h4.rutitr')
        super().add_field(field_name='post_content', css_selector='section.newsPageContent')
        super().add_field(field_name='post_subtitle', css_selector='div.newstitle > h4.rutitr')
        super().add_field(field_name='post_subtitle', css_selector='div.newstitle > h4.rutitr')

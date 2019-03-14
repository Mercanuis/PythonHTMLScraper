import htmlparse
import htmlFetch


class Parser:
    def __init__(self):
        pass

    @staticmethod
    def parse(url, target):
        f = htmlFetch.HTMLFetcher()
        data = f.get_from_url(url)

        h = htmlparse.HTMLParser()
        return h.parse_html(url, data, target)

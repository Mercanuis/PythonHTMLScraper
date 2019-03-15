"""
Simple parser, main engine for running program
This class calls the htmlparse and htmlfetcher scripts
"""
from html import htmlfetch, htmlparse


class Parser:
    def __init__(self):
        pass

    # Fetches the HTML from the given url and then parses it
    # url is the URL to be called
    # target is the word to be parsed and found from the HTML
    @staticmethod
    def parse(url, target):
        f = htmlfetch.HTMLFetcher()
        data = f.get_from_url(url)

        h = htmlparse.HTMLParser()
        return h.parse_html(url, data, target)

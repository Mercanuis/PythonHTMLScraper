"""
Class that helps with pulling the request from the given URL
Used to fetch the HTML
"""
import requests


class HTMLFetcher:
    def __init__(self):
        pass

    @staticmethod
    def get_from_url(url):
        req = requests.get(url)
        return req.text

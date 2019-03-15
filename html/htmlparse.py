"""
HTML parser, main engine for parsing HTML body into
usable token strings. Strips whitespace and HTML tags

Utilizes a db to try and optimize calls for prior hits. If
there is a record return the record, otherwise parse the HTML
provided and count the instances, then save to DB and return count
"""
from bs4 import BeautifulSoup
from database import db

html_parser = 'html.parser'

d = db.DB("~/PycharmProjects/Virtusize/database/db.json")


def get_from_db(url, target):
    # Gets from the database the value for the given URL and target
    # If there is no data returns False
    val = False
    val_map = d.get(url)
    if val_map is not False:
        for words in val_map:
            if words["word"] == target:
                val = words["count"]
                break
    return val


def get_target_count(data, target):
    # Gets the count from the given HTML data for the given target
    # Returns the count
    count = 0
    soup = BeautifulSoup(data, html_parser)
    for text_string in soup.stripped_strings:
        for text in text_string.split(" "):
            if text.lower() == target:
                count = count + 1
    return count


def write_to_db(url, target, count):
    # Writes to the db the given count for the given target, with the key URL
    value = {"word": target, "count": count}
    word_list = d.get(url)
    if word_list is False:
        word_list = [value]
    else:
        word_list.append(value)
    d.set(url, word_list)


class HTMLParser:
    def __init__(self):
        pass

    @staticmethod
    def parse_html(url, data, target):
        value = get_from_db(url, target)
        if value is not False:
            return value
        else:
            try:
                count = get_target_count(data, target)
                write_to_db(url, target, count)
                return count
            except Exception as e:
                print("html_parse: " + str(e))
                return e

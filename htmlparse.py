from bs4 import BeautifulSoup
import db

html_parser = 'html.parser'

d = db.DB("~/PycharmProjects/Virtusize/database/db.json")


class HTMLParser:
    def __init__(self):
        pass

    def parse_html(self, url, data, target):
        value = self.get_from_db(url, target)
        if value is not False:
            return value
        else:
            try:
                count = self.get_target_count(data, target)
                self.write_to_db(url, target, count)
                return count
            except Exception as e:
                print("html_parse: " + str(e))
                return e

    def get_from_db(self, url, target):
        val = False
        val_map = d.get(url)
        if val_map is not False:
            for words in val_map:
                if words["word"] == target:
                    val = words["count"]
                    break
        return val

    def write_to_db(self, url, target, count):
        value = {"word": target, "count": count}
        word_list = d.get(url)
        if word_list is False:
            word_list = [value]
        else:
            word_list.append(value)
        d.set(url, word_list)

    def get_target_count(self, data, target):
        count = 0
        soup = BeautifulSoup(data, html_parser)
        for text_string in soup.stripped_strings:
            for text in text_string.split(" "):
                if text.lower() == target:
                    count = count + 1
        return count

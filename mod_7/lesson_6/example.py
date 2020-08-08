from dataclasses import dataclass

from bs4 import BeautifulSoup
import requests


def is_a_and_has_rel_bookmark(tag):
    return tag.name == "a" and tag.has_attr("rel") and "bookmark" in tag["rel"]


def is_title_containing_tag(tag):
    return tag.name == "h2" and tag.has_attr("class") and "entry-title" in tag["class"]


def is_publish_date_containing_tag(tag):
    return tag.name == "time" and tag.has_attr("class") and "entry-date" in tag["class"] and "published" in tag["class"]


@dataclass
class PostPreview:
    publish_date: str
    title: str


class PyJazzParser:
    PAGE_URL = "https://www.pyjazz.pl"

    def __init__(self):
        self.parsed_page = None
        self.last_post_index = 0
        self.found_post_previews = []

    def load_page_html(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.parsed_page = BeautifulSoup(response.text, features="html.parser")

    # def show_example(self):
    #     # tag_p = self.parsed_page.p
    #     # print(tag_p)
    #     # print(tag_p.name)
    #     # print(tag_p.attrs)
    #     # print(tag_p.string)
    #     # time = self.parsed_page.div.time
    #     # print(self.parsed_page.div.find_all('time'))
    #     # print(time.contents)
    #     # print(time.parent)
    #     # print(time.previous_sibling)
    #     # print(time.next_sibling)
    #     print(self.parsed_page.find_all(is_a_and_has_rel_bookmark))

    def parse_all_previews(self):
        publish_date_tags = self.parsed_page.find_all(is_publish_date_containing_tag)
        title_tags = self.parsed_page.find_all(is_title_containing_tag)
        for publish_date_tag, title_tag in zip(publish_date_tags, title_tags):
            post_preview = PostPreview(publish_date_tag.string, title_tag.string)
            self.found_post_previews.append(post_preview)


def run_example():
    parser = PyJazzParser()
    parser.load_page_html()
    # parser.show_example()
    parser.parse_all_previews()
    print(parser.found_post_previews)


if __name__ == '__main__':
    run_example()




from dataclasses import dataclass

import requests


@dataclass
class PostPreview:
    publish_date: str
    title: str


class PyJazzParser:
    PAGE_URL = "https://www.pyjazz.pl"

    def __init__(self):
        self.page_html = None
        self.last_post_index = 0
        self.found_post_previews = []

    def load_page_html(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.page_html = response.text

    def parse_all_previews(self):
        while True:
            try:
                self.search_for_next_post_preview()
            except ValueError:
                return

    def search_for_next_post_preview(self):
        publish_date, publish_date_index = self._find_publish_date()
        title, title_index = self._find_title(publish_date_index)
        self.last_post_index = title_index
        self.found_post_previews.append(PostPreview(publish_date, title))

    def _find_publish_date(self):
        time_marker_open_begin = self.page_html.index('<time class="entry-date published', self.last_post_index)
        time_marker_open_end = self.page_html.index(">", time_marker_open_begin) + len(">")
        time_marker_close = self.page_html.index("</time>", time_marker_open_end)
        return self.page_html[time_marker_open_end:time_marker_close], time_marker_close

    def _find_title(self, publish_date_index):
        title_header_open = self.page_html.index('<h2 class="entry-title">', publish_date_index)
        title_url_open_end = self.page_html.index('rel="bookmark">', title_header_open) + len('rel="bookmark">')
        title_url_close = self.page_html.index("</a>", title_url_open_end)
        return self.page_html[title_url_open_end:title_url_close], title_url_close


def run_example():
    parser = PyJazzParser()
    parser.load_page_html()
    parser.parse_all_previews()
    print(parser.found_post_previews)


if __name__ == '__main__':
    run_example()

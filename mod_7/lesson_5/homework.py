
# Pobierz ze strony infoshareacademy.com informacje o liście kursów.
# Dla każdego kursu pozyskaj dane o jego nazwie, czasie trwania oraz jakiego jest typu (dzienny, wieczorowy, itd.)

from dataclasses import dataclass
from enum import Enum

import requests


class CourseType(Enum):
    DAILY_CLASS = "kurs dzienny"
    EVENING_CLASS = "kurs wieczorowy"
    WEEKEND_CLASS = "kurs weekendowy"


@dataclass
class CourseData:
    title: str
    number_of_hours: int
    type: CourseType


class InfoShareAcademyParser:
    PAGE_URL = "https://infoshareacademy.com/"

    def __init__(self):
        self.page_html = None
        self.last_course_index = 0
        self.found_courses = []

    def load_page_html(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.page_html = response.text

    def parse_all_courses(self):
        while True:
            try:
                self.search_for_next_course()
            except ValueError:
                return

    def search_for_next_course(self):
        title, title_index = self._find_title()
        number_of_hours, hours_index = self._find_duration(title_index)
        course_type, type_index = self._find_type(hours_index)
        self.last_course_index = type_index
        self.found_courses.append(CourseData(title, number_of_hours, course_type))

    def _find_title(self):
        logo_div_marker = self.page_html.index('<div class="courses-page__item__logo">', self.last_course_index)
        paragraph_marker_open_end = self.page_html.index('<p>', logo_div_marker) + len('<p>')
        paragraph_marker_close = self.page_html.index('</p>', paragraph_marker_open_end)
        return self.page_html[paragraph_marker_open_end:paragraph_marker_close], paragraph_marker_close

    def _find_duration(self, title_index):
        span_open_marker_begin = self.page_html.index('<span', title_index)
        span_open_marker_end = self.page_html.index('>', span_open_marker_begin) + len('>')
        span_close_marker = self.page_html.index('</span>', span_open_marker_end)
        duration_with_h_symbol = self.page_html[span_open_marker_end:span_close_marker]
        duration = duration_with_h_symbol.replace("h", "").strip()
        return int(duration), span_close_marker

    def _find_type(self, time_index):
        span_open_marker_begin = self.page_html.index('<span', time_index)
        span_open_marker_end = self.page_html.index('>', span_open_marker_begin) + len('>')
        span_close_marker = self.page_html.index('</span>', span_open_marker_end)
        course_type_description = self.page_html[span_open_marker_end:span_close_marker]
        course_type = CourseType(course_type_description)
        return course_type, span_close_marker


def run_example():
    parser = InfoShareAcademyParser()
    parser.load_page_html()
    parser.parse_all_courses()
    print(parser.found_courses)


if __name__ == '__main__':
    run_example()

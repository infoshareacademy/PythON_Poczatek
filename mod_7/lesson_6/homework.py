
# Zmodyfikuj rozwiązanie zadania z poprzedniej lekcji wykorzystując w swojej implementacji bibliotekę Beautiful Soup

from dataclasses import dataclass
from enum import Enum

import requests
from bs4 import BeautifulSoup


class CourseType(Enum):
    DAILY_CLASS = "kurs dzienny"
    EVENING_CLASS = "kurs wieczorowy"
    WEEKEND_CLASS = "kurs weekendowy"


@dataclass
class CourseData:
    title: str
    number_of_hours: int
    type: CourseType


def course_tile_div(tag):
    return tag.name == "div" and tag.has_attr("class") and "courses-page__item__inner" in tag["class"]


class InfoShareAcademyParser:
    PAGE_URL = "https://infoshareacademy.com/"

    def __init__(self):
        self.parsed_page = None
        self.last_course_index = 0
        self.found_courses = []

    def load_page_html(self):
        response = requests.get(self.PAGE_URL)
        response.raise_for_status()
        self.parsed_page = BeautifulSoup(response.text, features="html.parser")

    def parse_all_courses(self):
        course_tiles = self.parsed_page.find_all(course_tile_div)
        for course_tile in course_tiles:
            course_title_tag = course_tile.p
            title = course_title_tag.string
            course_span_tags = course_tile.find_all("span")
            duration_with_h_symbol = course_span_tags[0].string
            course_type_description = course_span_tags[1].string
            duration_str = duration_with_h_symbol.replace("h", "").strip()
            duration = int(duration_str)
            course_type = CourseType(course_type_description)
            course_data = CourseData(title=title, number_of_hours=duration, type=course_type)
            self.found_courses.append(course_data)


def run_example():
    parser = InfoShareAcademyParser()
    parser.load_page_html()
    parser.parse_all_courses()
    print(parser.found_courses)


if __name__ == '__main__':
    run_example()

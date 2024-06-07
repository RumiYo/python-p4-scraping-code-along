from bs4 import BeautifulSoup
import requests
from Course import Course
import ipdb


class Scraper:

    def __init__(self):
        self.courses = []

    def get_page(self):

        headers = {'user-agent': 'my-app/0.0.1'}
        html = requests.get("https://learn-co-curriculum.github.io/site-for-scraping/courses", headers=headers)
        doc = BeautifulSoup(html.text, 'html.parser')
        return doc

    def get_courses(self):
        return self.get_page().select('.post')

    def make_courses(self):
        courses = self.get_courses()
        for course in courses:
            title = course.select("h2")[0].text if course.select("h2") else ''
            date = course.select(".date")[0].text if course.select(".date") else ''
            description = course.select("p")[0].text if course.select("p") else ''

            new_course = Course(title, date, description)
            self.courses.append(new_course)
        return self.courses

    def print_courses(self):
        for course in self.make_courses():
            print(course)

import requests
import requests_html
from pprint import pprint

class RecipeScraper:

    def __init__(self):
        self.html_tags = []
        self.headers = []

    def __fetch_raw_data(self, url):
        session = requests_html.HTMLSession()
        r = session.get(url)
        return r

    def __find_class(self, rendered_html, class_name):
        data = rendered_html.html.find(class_name, first=True)
        return data.text

    def assemble_recipe(self, url):
        recipe_dict = {}
        raw_html = self.__fetch_raw_data(url)
        raw_html.html.render()

        for ind, val in enumerate(self.html_tags):
            recipe_dict[self.headers[ind]] = self.__find_class(raw_html, val)

        pprint(recipe_dict)
        return recipe_dict

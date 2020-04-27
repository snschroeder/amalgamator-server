import requests
import requests_html
from pprint import pprint

class RecipeScraper:

    def __fetch_raw_data(self, url):
        session = requests_html.HTMLSession()
        r = session.get(url)
        return r

    def __find_class(self, raw_html, class_name):
        # raw_html.html.render()
        data = raw_html.html.find(class_name, first=True)
        pprint(data.text)
        return data

    def assemble_recipe(self, url, class_arr):
        recipe_dict = {}
        headers = ['summary', 'ingredients', 'instructions']

        raw_html = self.__fetch_raw_data(url)
        raw_html.html.render()

        for ind, val in enumerate(class_arr):
            recipe_dict[headers[ind]] = self.__find_class(raw_html, val)

        pprint(recipe_dict)
        return recipe_dict


r_scraper = RecipeScraper()

test_url = 'https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/'
test_class_name = '.recipe-info-section' # correctly returns recipe summary
test2_class_name = '.ingredients-section' # correctly returns ingredients
test3_class_name = '.instructions-section' # correctly returns recipe instructions

test_arr = ['.recipe-info-section', '.ingredients-section', '.instructions-section']

r_scraper.assemble_recipe(test_url, test_arr)

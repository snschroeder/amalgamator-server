import requests
import requests_html
from pprint import pprint

class RecipeScraper:

    def fetch_raw_data(self, link):
        session = requests_html.HTMLSession()
        r = session.get(link)
        return r

    def find_class(self, raw_html, class_name):
        raw_html.html.render()
        data = raw_html.html.find(class_name, first=True)
        pprint(data.text)
        return data

r_scraper = RecipeScraper()

test_url = 'https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/'
test_class_name = '.recipe-info-section' # correctly returns recipe summary
test2_class_name = '.ingredients-section' # correctly returns ingredients
test3_class_name = '.instructions-section' # correctly returns recipe instructions


raw_html = r_scraper.fetch_raw_data(test_url)

r_scraper.find_class(raw_html, test2_class_name)

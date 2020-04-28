import requests
import requests_html
from pprint import pprint

class NYTCRecipeScraper:
    html_tags = [
        'title',
        '#content > div.recipe > div > article > div.recipe-intro > div.recipe-topnote-metadata > div.topnote > p:nth-child(1)', # topnote
        '#content > div.recipe > div > article > div.recipe-intro > div.recipe-topnote-metadata > div.topnote > p.related-article', # featured in
        '#content > div.recipe > div > article > div.recipe-metadata > div.tags-nutrition-container', # tags
        '#content > div.recipe > div > article > div.recipe-instructions > section.recipe-ingredients-wrap', # ingredients
        '#content > div.recipe > div > article > div.recipe-instructions > section.recipe-steps-wrap > ol', # instructions
        '#content > div.recipe > div > article > div.recipe-instructions > section.recipe-ingredients-wrap > ul:nth-child(7) > li > div > div.nutrition-tooltip > ul > li > div' # nutrition info
    ]

    headers = ['name', 'summary', 'featured in', 'tags', 'ingredients', 'instructions', 'nutrition info']

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


test_url = 'https://cooking.nytimes.com/recipes/1017347-italian-style-tuna-sandwich?smid=ck-recipe-iOS-share'


nyt_scraper = NYTCRecipeScraper()
nyt_scraper.assemble_recipe(test_url)

import requests
import requests_html
from pprint import pprint
from recipe_scraper import RecipeScraper

class NYTCRecipeScraper(RecipeScraper):
    def __init__(self):
        self.html_tags = [
            'title',
            '#content > div.recipe > div > article > div.recipe-intro > div.recipe-topnote-metadata > div.topnote > p:nth-child(1)', # topnote
            '#content > div.recipe > div > article > div.recipe-intro > div.recipe-topnote-metadata > div.topnote > p.related-article', # featured in
            '#content > div.recipe > div > article > div.recipe-metadata > div.tags-nutrition-container', # tags
            '#content > div.recipe > div > article > div.recipe-instructions > section.recipe-ingredients-wrap', # ingredients
            '#content > div.recipe > div > article > div.recipe-instructions > section.recipe-steps-wrap > ol', # instructions
            '#content > div.recipe > div > article > div.recipe-instructions > section.recipe-ingredients-wrap > ul:nth-child(7) > li > div > div.nutrition-tooltip > ul > li > div' # nutrition info
        ]
        self.headers = ['name', 'summary', 'featured in', 'tags', 'ingredients', 'instructions', 'nutrition info']


test_url = 'https://cooking.nytimes.com/recipes/1017347-italian-style-tuna-sandwich?smid=ck-recipe-iOS-share'


nyt_scraper = NYTCRecipeScraper()
nyt_scraper.assemble_recipe(test_url)

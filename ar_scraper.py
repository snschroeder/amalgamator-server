import requests
import requests_html
from pprint import pprint
from recipe_scraper import RecipeScraper

class ARRecipeScraper(RecipeScraper):
    def __init__(self):
        self.html_tags = [
            'title',
            '.recipe-info-section',
            '.ingredients-section',
            '.instructions-section',
            'body > div.docked-sharebar-content-container > div > main > div.recipe-container.two-col-container > div.content.two-col-main-content.karma-content-container > div.recipe-content.two-col-content.karma-main-column > div.two-col-content-wrapper > div.recipe-content-container > section.nutrition-section.container > div > div.section-body'
        ]
        self.headers = ['name', 'summary', 'ingredients', 'instructions', 'nutrition info']


# these timeout before resolving
test6_url = 'https://www.allrecipes.com/recipe/98390/megans-granola/'
test2_url = 'https://www.allrecipes.com/recipe/21459/indian-dahl-with-spinach/'

# these work correctly
test5_url = 'https://www.allrecipes.com/recipe/228293/curry-stand-chicken-tikka-masala-sauce/'
test4_url = 'https://www.allrecipes.com/recipe/9023/baked-teriyaki-chicken/'
test3_url = 'https://www.allrecipes.com/recipe/10549/best-brownies/'
test_url = 'https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/'

ar_scraper = ARRecipeScraper()
ar_scraper.assemble_recipe(test3_url)

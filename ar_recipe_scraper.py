import requests
import requests_html
from pprint import pprint

class ARRecipeScraper:
    html_tags = [
        'title',
        '.recipe-info-section',
        '.ingredients-section',
        '.instructions-section',
        'body > div.docked-sharebar-content-container > div > main > div.recipe-container.two-col-container > div.content.two-col-main-content.karma-content-container > div.recipe-content.two-col-content.karma-main-column > div.two-col-content-wrapper > div.recipe-content-container > section.nutrition-section.container > div > div.section-body'
    ]
    headers = ['name', 'summary', 'ingredients', 'instructions', 'nutrition info']

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


r_scraper = ARRecipeScraper()

# these timeout before resolving
test6_url = 'https://www.allrecipes.com/recipe/98390/megans-granola/'
test2_url = 'https://www.allrecipes.com/recipe/21459/indian-dahl-with-spinach/'

# these work correctly
test5_url = 'https://www.allrecipes.com/recipe/228293/curry-stand-chicken-tikka-masala-sauce/'
test4_url = 'https://www.allrecipes.com/recipe/9023/baked-teriyaki-chicken/'
test3_url = 'https://www.allrecipes.com/recipe/10549/best-brownies/'
test_url = 'https://www.allrecipes.com/recipe/10813/best-chocolate-chip-cookies/'
# test_class_name = '.recipe-info-section' # correctly returns recipe summary
# test2_class_name = '.ingredients-section' # correctly returns ingredients
# test3_class_name = '.instructions-section' # correctly returns recipe instructions
# nutrition_selector = 'body > div.docked-sharebar-content-container > div > main > div.recipe-container.two-col-container > div.content.two-col-main-content.karma-content-container > div.recipe-content.two-col-content.karma-main-column > div.two-col-content-wrapper > div.recipe-content-container > section.nutrition-section.container > div > div.section-body'
#
# test_arr = ['.recipe-info-section', '.ingredients-section', '.instructions-section', nutrition_selector]

r_scraper.assemble_recipe(test_url)

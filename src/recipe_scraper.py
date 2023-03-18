import sys

import requests

from bs4 import BeautifulSoup
from requests import RequestException

from src.recipe import Recipe


class RecipeScraper:
    """
    Scrap recipe page from Kwestia Smaku to find details about ingredients.

    The RecipeScraper should only attempt to find ingredients information
    and should not process any additional details, such as steps to create a recipe
    or pictures.
    """

    _DEFAULT_PARSER = "lxml"

    def __init__(self, recipe_url: str):
        self.recipe_url = recipe_url

    def _get_recipe_page(self) -> str:
        try:
            recipe_page_response = requests.get(self.recipe_url, timeout=1)
            if recipe_page_response.status_code == requests.codes.ok:
                return recipe_page_response.text
            else:
                raise ConnectionError

        except* (RequestException, ConnectionError) as request_error:
            print(f"Error while trying to connect to the website.\n{request_error}")
            sys.exit(1)

    def _get_ingredients_details(self, recipe_text: str) -> Recipe:
        soup = BeautifulSoup(recipe_text, self._DEFAULT_PARSER)

        servings: str = soup.select(".field-name-field-ilosc-porcji")[0].text.strip()
        ingredients_elements = soup.select_one(".field-name-field-skladniki").select(
            "li"
        )
        ingredients = [ingredient.text.strip() for ingredient in ingredients_elements]

        return Recipe(servings, ingredients)

    def get_recipe(self) -> Recipe:
        recipe_text = self._get_recipe_page()
        recipe = self._get_ingredients_details(recipe_text)
        return recipe


if __name__ == "__main__":
    scraper = RecipeScraper(
        "https://www.kwestiasmaku.com/kuchnia_polska/rosol/przepis.html"
    )
    scrapped_recipe = scraper.get_recipe()
    print(scrapped_recipe)

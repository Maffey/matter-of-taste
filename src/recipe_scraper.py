from typing import Any
import requests

from bs4 import BeautifulSoup

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
            recipe_page = requests.get(self.recipe_url, timeout=1)
            # TODO check for error response codes
            return recipe_page.text

        # TODO make messages consistent.
        #  refactor using exception groups or just extract the error message printing.
        except requests.URLRequired as url_error:
            print(f"Problem with url. Error: {url_error}.")
        except requests.Timeout as timeout_error:
            print(f"Request or server response timeout. Error: {timeout_error}.")
        except ConnectionError as connection_error:
            print(
                f"There have been problems with connection to the site with error {connection_error}."
            )
        except requests.TooManyRedirects as redirects_error:
            print(f"Too many redirects with error {redirects_error}.")
        except requests.HTTPError as http_error:
            print(f"HTTP error occurred with error: {http_error}.")
        # TODO stop execution if exception occurs

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

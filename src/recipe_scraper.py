from typing import Any
import requests

from bs4 import BeautifulSoup


# TODO here or in scraper, normalize strings (to lower etc.)
def normalize_data(recipe: dict[str, Any]) -> dict[str, Any]:
    pass


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
        self._ingredients = None

    def _get_recipe_page(self) -> str:
        try:
            recipe_page = requests.get(self.recipe_url, timeout=1)
            # TODO check for error response codes
            return recipe_page.text
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

    def _extract_ingredients_details(
        self, recipe_text: str
    ) -> dict[str, str | list[str]]:
        soup = BeautifulSoup(recipe_text, self._DEFAULT_PARSER)

        portions: str = soup.select(".field-name-field-ilosc-porcji")[0].text.strip()
        ingredients_elements = soup.select_one(".field-name-field-skladniki").select(
            "li"
        )
        ingredients = [ingredient.text.strip() for ingredient in ingredients_elements]

        return {"portions": portions, "ingredients": ingredients}

    def get_recipe(self):
        recipe_text = self._get_recipe_page()
        ingredients_details = self._extract_ingredients_details(recipe_text)
        # TODO refactor this, maybe move extract_ingredients_details to here
        return ingredients_details


if __name__ == "__main__":
    scraper = RecipeScraper(
        "https://www.kwestiasmaku.com/kuchnia_polska/rosol/przepis.html"
    )
    soup = scraper.get_recipe()
    print(soup)

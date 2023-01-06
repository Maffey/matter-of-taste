import requests

from bs4 import BeautifulSoup

class RecipeScraper:
    """
    Scrap recipe page from Kwestia Smaku to find details about ingredients.
    
    The RecipeScraper should only attempt to find ingredients information
    and should not process any additional details, such as steps to create a recipe
    or pictures.
    """
    DEFAULT_PARSER = "lxml"

    def __init__(self, recipe_url: str):
        self.recipe_url = recipe_url
        self._ingredients = None

    def _get_recipe_page(self) -> str:
        recipe_page = requests.get(self.recipe_url)
        return recipe_page.text
    
    def _extract_ingredients_details(self, recipe_text: str):
        soup = BeautifulSoup(recipe_text, self.DEFAULT_PARSER)
        # TODO return actual ingredients
        # <div class="group-skladniki field-group-div"><h3><span>Składniki</span></h3>
        # porcje: .field-name-field-ilosc-porcji
        # skladniki: .field-name-field-skladniki
        portions = soup.select(".field-name-field-ilosc-porcji")
        ingredients = soup.select(".field-name-field-skladniki")
        print(portions, ingredients)
        return soup

    def get_ingredients(self):
        recipe_text = self._get_recipe_page()
        ingredients_details = self._extract_ingredients_details(recipe_text)
        # TODO
        return ingredients_details
    
if __name__ == "__main__":
    scraper = RecipeScraper("https://www.kwestiasmaku.com/kuchnia_polska/rosol/przepis.html")
    soup = scraper.get_ingredients()
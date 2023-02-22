from typing import Any
from translate import Translator

from src.recipe_scraper import SERVINGS, INGREDIENTS, normalize_recipe_data


# TODO needs to:
#  - from list of ingredients, extract actual ingredients (sometimes there are few per entry)
#  - from element in the list, extract information about the actual food
#  - extract information about a portion
#  should NLP be used??
class RecipeTranslator:
    _POLISH_LOCALE = "pl"
    _ENGLISH_LOCALE = "en"

    def translate_recipe_to_english(self, recipe: dict[str, Any]) -> dict[str, Any]:
        translator = Translator(
            from_lang=self._POLISH_LOCALE, to_lang=self._ENGLISH_LOCALE
        )
        recipe[SERVINGS] = translator.translate(recipe[SERVINGS])
        translated_ingredients = [
            translator.translate(ingredient)
            for ingredient in recipe[INGREDIENTS]
        ]
        recipe[INGREDIENTS] = translated_ingredients
        return normalize_recipe_data(recipe)


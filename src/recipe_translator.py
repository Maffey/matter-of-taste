# TODO needs to:
# - from list of ingredients, extract actual ingredients (sometimes there are few per entry)
# - from element in the list, extract information about the actual food
# - extract information about a portion
# TODO should NLP be used??
from typing import Any
from translate import Translator


class RecipeTranslator:
    _SOURCE_LOCALE = "pl"
    _TARGET_LOCALE = "en"

    def translate_recipe_to_english(self, recipe: dict[str, Any]) -> dict[str, Any]:
        translator = Translator(
            from_lang=self._SOURCE_LOCALE, to_lang=self._TARGET_LOCALE
        )
        recipe["portions"] = translator.translate(recipe["portions"]).lower()
        translated_ingredients = [
            translator.translate(ingredient).lower()
            for ingredient in recipe["ingredients"]
        ]
        recipe["ingredients"] = translated_ingredients
        return recipe

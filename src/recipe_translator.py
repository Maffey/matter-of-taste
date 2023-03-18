from translate import Translator

from src.recipe import Recipe


# TODO needs to:
#  - from list of ingredients,
#  extract actual ingredients (sometimes there are few per entry)
#  - from element in the list, extract information about the actual food
#  - extract information about a portion
#  should NLP be used??
class RecipeTranslator:
    _POLISH_LOCALE = "pl"
    _ENGLISH_LOCALE = "en"

    def translate_recipe_to_english(self, recipe: Recipe) -> Recipe:
        translator = Translator(
            from_lang=self._POLISH_LOCALE, to_lang=self._ENGLISH_LOCALE
        )
        recipe.servings = translator.translate(recipe.servings)
        recipe.ingredients = [
            translator.translate(ingredient) for ingredient in recipe.ingredients
        ]
        return recipe

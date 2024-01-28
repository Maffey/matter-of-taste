import string

import nltk
from translate import Translator

from src.models.recipe import Recipe, TokenizedRecipe

# TODO needs to:
#  - from list of ingredients,
#  extract actual ingredients (sometimes there are few per entry)
#  - from element in the list, extract information about the actual food
#  - extract information about a portion
#  should NLP be used??

_POLISH_LOCALE = "pl"
_ENGLISH_LOCALE = "en"

_STOP_WORDS = set(nltk.corpus.stopwords.words("english"))


def translate_recipe_to_english(recipe: Recipe) -> Recipe:
    translator = Translator(from_lang=_POLISH_LOCALE, to_lang=_ENGLISH_LOCALE)
    if recipe.servings:
        recipe.servings = translator.translate(recipe.servings)
    recipe.ingredients = [
        translator.translate(ingredient) for ingredient in recipe.ingredients
    ]
    return recipe


def tokenize_recipe(recipe: Recipe) -> TokenizedRecipe:
    _drop_punctuation_from_ingredients(recipe)
    if recipe.servings:
        word_tokens_servings = nltk.word_tokenize(recipe.servings)
        filtered_word_tokens_servings = " ".join(
            [
                word
                for word in word_tokens_servings
                if word.casefold() not in _STOP_WORDS
            ]
        )
    else:
        filtered_word_tokens_servings = None

    word_tokens_ingredients = [
        nltk.word_tokenize(ingredient) for ingredient in recipe.ingredients
    ]
    filtered_tokenized_ingredients = []
    for ingredient in word_tokens_ingredients:
        ingredient_tokens = " ".join(
            [word for word in ingredient if word.casefold() not in _STOP_WORDS]
        )
        filtered_tokenized_ingredients.append(ingredient_tokens)

    return TokenizedRecipe(
        filtered_word_tokens_servings, filtered_tokenized_ingredients
    )


def _drop_punctuation_from_ingredients(recipe: Recipe) -> None:
    recipe.ingredients = [
        ingredient.translate(str.maketrans("", "", string.punctuation))
        for ingredient in recipe.ingredients
    ]


if __name__ == "__main__":
    # Use this to install required dependencies for nltk
    nltk.download("punkt")
    nltk.download("stopwords")
    nltk.download("corpus")

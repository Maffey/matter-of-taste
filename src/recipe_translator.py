import string

import nltk
from translate import Translator

from src.models.recipe import Recipe, TokenizedRecipe

nltk.download("punkt")
nltk.download("stopwords")
nltk.download("corpus")


# TODO needs to:
#  - from list of ingredients,
#  extract actual ingredients (sometimes there are few per entry)
#  - from element in the list, extract information about the actual food
#  - extract information about a portion
#  should NLP be used??

_POLISH_LOCALE = "pl"
_ENGLISH_LOCALE = "en"


def translate_recipe_to_english(recipe: Recipe) -> Recipe:
    translator = Translator(from_lang=_POLISH_LOCALE, to_lang=_ENGLISH_LOCALE)
    recipe.servings = translator.translate(recipe.servings)
    recipe.ingredients = [
        translator.translate(ingredient) for ingredient in recipe.ingredients
    ]
    return recipe


def tokenize_recipe(recipe: Recipe) -> TokenizedRecipe:
    word_tokens_servings = nltk.word_tokenize(recipe.servings)
    drop_punctuation_from_ingredients(recipe)
    word_tokens_ingredients = [
        nltk.word_tokenize(ingredient) for ingredient in recipe.ingredients
    ]
    stop_words = set(nltk.corpus.stopwords.words("english"))
    filtered_word_tokens_servings = [
        word for word in word_tokens_servings if word.casefold() not in stop_words
    ]
    filtered_tokenized_ingredients = []
    for ingredient in word_tokens_ingredients:
        ingredient_tokens = [
            word for word in ingredient if word.casefold() not in stop_words
        ]
        filtered_tokenized_ingredients.append(ingredient_tokens)

    return TokenizedRecipe(
        filtered_word_tokens_servings, filtered_tokenized_ingredients
    )


def drop_punctuation_from_ingredients(recipe: Recipe) -> None:
    recipe.ingredients = [
        ingredient.translate(str.maketrans("", "", string.punctuation))
        for ingredient in recipe.ingredients
    ]

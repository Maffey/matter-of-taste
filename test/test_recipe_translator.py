import pytest

from src.recipe_translator import RecipeTranslator


def test_ingredients_are_properly_translated():
    recipe_translator = RecipeTranslator()
    polish_ingredients = {
        "portions": "1 porcja",
        "ingredients": ["1 kurczak", "wołowina", "woda"],
    }
    expected_ingredients = {
        "portions": "1 serving",
        "ingredients": ["1 chicken", "bovine meat", "water"],
    }

    english_ingredients = recipe_translator.translate_recipe_to_english(
        polish_ingredients
    )

    assert english_ingredients == expected_ingredients

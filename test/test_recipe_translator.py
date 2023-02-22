import pytest

from src.recipe_translator import RecipeTranslator
from conftest import build_recipe


@pytest.fixture
def recipe_translator():
    return RecipeTranslator()


@pytest.mark.parametrize(
    "servings, ingredients, expected_servings, expected_ingredients",
    [
        (
            "1 porcja",
            ["1 kurczak", "wołowina", "woda"],
            "1 serving",
            ["1 chicken", "bovine meat", "water"],
        )
    ],
)
def test_recipe_is_properly_translated(
    recipe_translator, servings, ingredients, expected_servings, expected_ingredients
):
    recipe = build_recipe(servings, ingredients)
    expected_recipe = build_recipe(expected_servings, expected_ingredients)

    translated_recipe = recipe_translator.translate_recipe_to_english(recipe)

    assert translated_recipe == expected_recipe

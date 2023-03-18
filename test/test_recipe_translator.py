import pytest

from src.recipe import Recipe
from src.recipe_translator import RecipeTranslator


@pytest.fixture
def recipe_translator():
    return RecipeTranslator()


@pytest.mark.parametrize(
    "recipe, expected_recipe",
    [
        (
            Recipe("1 porcja", ["1 kurczak", "wołowina", "woda"]),
            Recipe("1 serving", ["1 chicken", "beef", "water"]),
        )
    ],
)
def test_recipe_is_properly_translated(recipe_translator, recipe, expected_recipe):
    # This test might be brittle. "Wołowina" can be translated to either "beef" or "bovine meat".
    translated_recipe = recipe_translator.translate_recipe_to_english(recipe)
    assert translated_recipe == expected_recipe

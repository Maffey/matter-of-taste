import pytest

from src.recipe_translator import RecipeTranslator


@pytest.fixture
def recipe_translator():
    return RecipeTranslator()


@pytest.mark.parametrize(
    "portions, ingredients, expected_portions, expected_ingredients",
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
    recipe_translator, portions, ingredients, expected_portions, expected_ingredients
):
    recipe = {
        "portions": portions,
        "ingredients": ingredients,
    }
    expected_recipe = {
        "portions": expected_portions,
        "ingredients": expected_ingredients,
    }

    translated_recipe = recipe_translator.translate_recipe_to_english(recipe)

    assert translated_recipe == expected_recipe

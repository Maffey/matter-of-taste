import pytest

from src.recipe_scraper import  normalize_recipe_data
from conftest import build_recipe


@pytest.mark.parametrize(
    "servings, ingredients, expected_servings, expected_ingredients",
    [
        (
            " 2 PORCJE",
            ["Ziemniaki", " INDYK "],
            "2 porcje",
            ["ziemniaki", "indyk"],
        )
    ],
)
def test_normalize_data(servings, ingredients, expected_servings, expected_ingredients):
    recipe = build_recipe(servings, ingredients)
    expected_recipe = build_recipe(expected_servings, expected_ingredients)

    assert normalize_recipe_data(recipe) == expected_recipe

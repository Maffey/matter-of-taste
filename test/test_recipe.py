import pytest

from src.recipe import Recipe


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
def test_recipe_data_is_normalized(
    servings, ingredients, expected_servings, expected_ingredients
):
    recipe = Recipe(servings, ingredients)

    assert recipe.servings == expected_servings
    assert recipe.ingredients == expected_ingredients

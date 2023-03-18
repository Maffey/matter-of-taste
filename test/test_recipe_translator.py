import pytest

from src.recipe import Recipe
from src.recipe_translator import translate_recipe_to_english, tokenize_recipe


@pytest.mark.parametrize(
    "recipe, expected_recipe",
    [
        (
            Recipe("1 porcja", ["1 kurczak", "wołowina", "woda"]),
            Recipe("1 serving", ["1 chicken", "beef", "water"]),
        ),
    ],
)
def test_recipe_is_translated(recipe, expected_recipe):
    # This test might be brittle.
    # "Wołowina" can be translated to either "beef" or "bovine meat".
    translated_recipe = translate_recipe_to_english(recipe)
    assert translated_recipe == expected_recipe


@pytest.mark.parametrize(
    "recipe, expected_tokenized_servings, expected_tokenized_ingredients",
    [
        (
            Recipe(
                "Serves 6",
                [
                    "1 chicken weighing about 2 kg",
                    "300 g beef",
                    "3 litres of water",
                    "2 carrots, 1 parsley, 1 onion, 2 sprigs of "
                    "parsley, piece of celery, leek, cabbage leaf optional",
                    "spices: 1 tbsp sea salt, 3 grains of English herb, 1 bay "
                    "leaf, 4 whole peppercorns",
                ],
            ),
            ["serves", "6"],
            [
                ["1", "chicken", "weighing", "2", "kg"],
                ["300", "g", "beef"],
                ["3", "litres", "water"],
                [
                    "2",
                    "carrots",
                    ",",
                    "1",
                    "parsley",
                    ",",
                    "1",
                    "onion",
                    ",",
                    "2",
                    "sprigs",
                    "parsley",
                    ",",
                    "piece",
                    "celery",
                    ",",
                    "leek",
                    ",",
                    "cabbage",
                    "leaf",
                    "optional",
                ],
                [
                    "spices",
                    ":",
                    "1",
                    "tbsp",
                    "sea",
                    "salt",
                    ",",
                    "3",
                    "grains",
                    "english",
                    "herb",
                    ",",
                    "1",
                    "bay",
                    "leaf",
                    ",",
                    "4",
                    "whole",
                    "peppercorns",
                ],
            ],
        )
    ],
)
def test_recipe_is_tokenized(
    recipe,
    expected_tokenized_servings,
    expected_tokenized_ingredients,
):
    tokenized_recipe = tokenize_recipe(recipe)
    assert tokenized_recipe.servings == expected_tokenized_servings
    assert tokenized_recipe.ingredients == expected_tokenized_ingredients

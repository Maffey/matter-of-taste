import pytest

from src.recipe_scraper import SERVINGS, INGREDIENTS, RecipeType


def build_recipe(portions: str, ingredients: list[str]) -> RecipeType:
    return {
        SERVINGS: portions,
        INGREDIENTS: ingredients,
    }
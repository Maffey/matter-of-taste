from dataclasses import dataclass
from typing import Any


@dataclass
class BaseRecipe:
    servings: Any
    ingredients: Any

    def __eq__(self, other):
        return bool(
            self.servings == other.servings and self.ingredients == other.ingredients
        )


@dataclass
class Recipe(BaseRecipe):
    servings: str
    ingredients: list[str]

    def __post_init__(self):
        """Normalize Recipe data to have consistent text."""
        self.servings = self.servings.strip().lower()
        self.ingredients = [
            ingredient.strip().lower() for ingredient in self.ingredients
        ]


@dataclass
class TokenizedRecipe(BaseRecipe):
    servings: list[str]
    ingredients: list[list[str]]

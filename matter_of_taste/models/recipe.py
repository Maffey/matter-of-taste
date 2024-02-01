from dataclasses import dataclass
from typing import Optional


@dataclass
class BaseRecipe:
    servings: Optional[str]
    ingredients: list[str]

    def __eq__(self, other):
        return bool(
            self.servings == other.servings and self.ingredients == other.ingredients
        )


@dataclass
class Recipe(BaseRecipe):
    def __post_init__(self):
        """Normalize Recipe data to have consistent text."""
        if self.servings:
            self.servings = self.servings.strip().lower()
        self.ingredients = [
            ingredient.strip().lower() for ingredient in self.ingredients
        ]


@dataclass
class TokenizedRecipe(BaseRecipe):
    pass

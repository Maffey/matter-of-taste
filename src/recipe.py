from dataclasses import dataclass


@dataclass
class Recipe:
    servings: str
    ingredients: list[str]

    def __post_init__(self):
        """Normalize Recipe data to have consistent text."""
        self.servings = self.servings.strip().lower()
        self.ingredients = [
            ingredient.strip().lower() for ingredient in self.ingredients
        ]

    def __eq__(self, other):
        return bool(
            self.servings == other.servings and self.ingredients == other.ingredients
        )

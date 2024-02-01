from dataclasses import dataclass
from typing import Optional

from matter_of_taste.models.nutrition_result import NutritionInformation


@dataclass
class NutritionReport:
    recipe_name: str
    url: str
    servings: Optional[int]
    summary: NutritionInformation
    ingredients: list[NutritionInformation]

    def __str__(self):
        return (
            f"Recipe: {self.recipe_name}\n"
            f"URL: {self.url}\n"
            f"Servings: {self.servings}\n"
            f"Summary: {self.summary}\n"
            "\nIngredients:\n"
            + "\n".join([f"- {ingredient}" for ingredient in self.ingredients])
        )

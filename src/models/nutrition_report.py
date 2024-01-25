from dataclasses import dataclass

from src.models.nutrition_result import NutritionInformation


@dataclass
class NutritionReport:
    recipe_name: str
    url: str
    servings: int
    summary: NutritionInformation
    ingredients: list[NutritionInformation]

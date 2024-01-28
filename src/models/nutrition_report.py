from dataclasses import dataclass
from typing import Optional

from src.models.nutrition_result import NutritionInformation


@dataclass
class NutritionReport:
    recipe_name: str
    url: str
    servings: Optional[int]
    summary: NutritionInformation
    ingredients: list[NutritionInformation]

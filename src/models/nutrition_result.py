from dataclasses import dataclass


@dataclass
class NutritionResult:
    name: str
    calories: float
    serving_size_g: float
    carbohydrates_total_g: float
    sugar_g: float
    fat_total_g: float
    fat_saturated_g: float
    protein_g: float
    fiber_g: float
    sodium_mg: int
    potassium_mg: int
    cholesterol_mg: int

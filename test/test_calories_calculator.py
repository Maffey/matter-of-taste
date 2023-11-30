from src.calories_calculator import CaloriesCalculator
from src.models.nutrition_result import NutritionResult


def test_getting_nutritients_for_single_products():
    nutrition_info = CaloriesCalculator.get_nutrition_information("beef")
    assert nutrition_info == [
        NutritionResult(
            name="beef",
            calories=291.9,
            serving_size_g=100.0,
            carbohydrates_total_g=0.0,
            sugar_g=0.0,
            fat_total_g=19.7,
            fat_saturated_g=7.8,
            protein_g=26.6,
            fiber_g=0.0,
            sodium_mg=63,
            potassium_mg=206,
            cholesterol_mg=87,
        ),
    ]

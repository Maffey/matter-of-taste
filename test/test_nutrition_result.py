from src.models.nutrition_result import get_empty_nutrition_result, NutritionResult


def test_get_empty_nutrition_result():
    nutrition_result = get_empty_nutrition_result("foo")
    assert nutrition_result == NutritionResult(
        name="foo",
        calories=0.0,
        carbohydrates_total_g=0.0,
        sugar_g=0.0,
        fat_total_g=0.0,
        protein_g=0.0,
    )


def test_add_two_nutrition_results():
    nutrition_result1 = NutritionResult(
        name="a",
        calories=5.0,
        carbohydrates_total_g=1.0,
        sugar_g=5.0,
        fat_total_g=5.0,
        protein_g=10.0,
    )
    nutrition_result2 = NutritionResult(
        name="b",
        calories=5.0,
        carbohydrates_total_g=1.0,
        sugar_g=5.0,
        fat_total_g=5.0,
        protein_g=3.0,
    )
    assert nutrition_result1 + nutrition_result2 == NutritionResult(
        name="sum",
        calories=10.0,
        carbohydrates_total_g=2.0,
        sugar_g=10.0,
        fat_total_g=10.0,
        protein_g=13.0,
    )


def test_iadd_two_nutrition_results():
    nutrition_result1 = NutritionResult(
        name="a",
        calories=5.0,
        carbohydrates_total_g=1.0,
        sugar_g=5.0,
        fat_total_g=5.0,
        protein_g=10.0,
    )
    nutrition_result2 = NutritionResult(
        name="b",
        calories=5.0,
        carbohydrates_total_g=1.0,
        sugar_g=5.0,
        fat_total_g=5.0,
        protein_g=3.0,
    )

    nutrition_result1 += nutrition_result2

    assert nutrition_result1 == NutritionResult(
        name="a",
        calories=10.0,
        carbohydrates_total_g=2.0,
        sugar_g=10.0,
        fat_total_g=10.0,
        protein_g=13.0,
    )

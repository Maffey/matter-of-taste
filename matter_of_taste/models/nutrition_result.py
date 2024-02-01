from dataclasses import dataclass


@dataclass
class NutritionInformation:
    name: str
    calories: float
    carbohydrates_total_g: float
    sugar_g: float
    fat_total_g: float
    protein_g: float

    def __str__(self):
        return (
            f"Name: {self.name}\n"
            f"Calories: {self.calories} kcal\n"
            f"Carbohydrates: {self.carbohydrates_total_g} g\n"
            f"Sugar: {self.sugar_g} g\n"
            f"Fat: {self.fat_total_g} g\n"
            f"Protein: {self.protein_g} g"
        )

    def __add__(self, other: "NutritionInformation") -> "NutritionInformation":
        return NutritionInformation(
            name="sum",
            calories=self.calories + other.calories,
            carbohydrates_total_g=self.carbohydrates_total_g
            + other.carbohydrates_total_g,
            sugar_g=self.sugar_g + other.sugar_g,
            fat_total_g=self.fat_total_g + other.fat_total_g,
            protein_g=self.protein_g + other.protein_g,
        )

    def __iadd__(self, other: "NutritionInformation") -> "NutritionInformation":
        self.calories += other.calories
        self.carbohydrates_total_g += other.carbohydrates_total_g
        self.sugar_g += other.sugar_g
        self.fat_total_g += other.fat_total_g
        self.protein_g += other.protein_g
        return self


def get_empty_nutrition_result(name: str):
    return NutritionInformation(
        name=name,
        calories=0.0,
        carbohydrates_total_g=0.0,
        sugar_g=0.0,
        fat_total_g=0.0,
        protein_g=0.0,
    )

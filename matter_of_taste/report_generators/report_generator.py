from abc import ABC, abstractmethod

from matter_of_taste.models.nutrition_report import NutritionReport


class ReportGenerator(ABC):
    _INGREDIENTS_UNIT_SUFFIX = " (g)"
    _REPORT_HEADERS = (
        "Recipe Name",
        "URL",
        "Servings",
        "Calories (kcal)",
        f"Carbohydrates{_INGREDIENTS_UNIT_SUFFIX}",
        f"Sugar{_INGREDIENTS_UNIT_SUFFIX}",
        f"Fat{_INGREDIENTS_UNIT_SUFFIX}",
        f"Protein{_INGREDIENTS_UNIT_SUFFIX}",
    )

    def __init__(self, nutrition_report: NutritionReport) -> None:
        self.nutrition_report = nutrition_report

    @abstractmethod
    def generate(self) -> None:
        # TODO add target param to select file
        ...

    def _get_nutrition_report_data(self) -> tuple:
        report = self.nutrition_report
        summary = report.summary
        summary_data = (
            summary.calories,
            summary.carbohydrates_total_g,
            summary.sugar_g,
            summary.fat_total_g,
            summary.protein_g,
        )
        return report.recipe_name, report.url, report.servings, *summary_data

    @staticmethod
    def _stringify_all_report_elements(data_row: tuple) -> tuple[str, ...]:
        return tuple(str(element) for element in data_row)

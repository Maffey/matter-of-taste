import csv

from matter_of_taste.report_generators.report_generator import ReportGenerator


class CsvReportGenerator(ReportGenerator):
    _DEFAULT_FILE_NAME = "report.csv"
    _INGREDIENTS_UNIT_SUFFIX = " (g)"
    _REPORT_HEADER = (
        "Recipe Name",
        "URL",
        "Servings",
        "Calories (kcal)",
        f"Carbohydrates{_INGREDIENTS_UNIT_SUFFIX}",
        f"Sugar{_INGREDIENTS_UNIT_SUFFIX}",
        f"Fat{_INGREDIENTS_UNIT_SUFFIX}",
        f"Protein{_INGREDIENTS_UNIT_SUFFIX}",
    )

    def generate(self) -> None:
        # TODO add target param to select file
        with open(self._DEFAULT_FILE_NAME, "w", newline="") as report_file:
            report_writer = csv.writer(report_file)
            report_writer.writerow(self._REPORT_HEADER)
            report_writer.writerow(self.get_nutrition_report_csv_data())

    def get_nutrition_report_csv_data(self) -> tuple:
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

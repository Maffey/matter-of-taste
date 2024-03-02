import csv

from matter_of_taste.report_generators.report_generator import ReportGenerator


class CsvReportGenerator(ReportGenerator):
    _DEFAULT_FILE_NAME = "report.csv"

    def generate(self) -> None:
        with open(self._DEFAULT_FILE_NAME, "w", newline="") as report_file:
            report_writer = csv.writer(report_file)
            report_writer.writerow(self._REPORT_HEADERS)
            report_writer.writerow(self._get_nutrition_report_data())

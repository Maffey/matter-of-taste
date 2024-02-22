from rich import print

from matter_of_taste.report_generators.report_generator import ReportGenerator


class StdoutReportGenerator(ReportGenerator):
    def generate(self) -> None:
        print(f"[blue]{self.nutrition_report}[/blue]")

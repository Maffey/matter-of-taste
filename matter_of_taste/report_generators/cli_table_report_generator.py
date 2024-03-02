from rich.console import Console
from rich.table import Table

from matter_of_taste.report_generators.report_generator import ReportGenerator


class CliTableReportGenerator(ReportGenerator):
    def generate(self) -> None:
        console = Console()
        console.print(self._build_table_structure())

    def _build_table_structure(self) -> Table:
        table = Table(show_header=True, header_style="bold magenta")
        for column_name in self._REPORT_HEADERS:
            table.add_column(column_name, style="dim")
        table.add_row(
            *self._stringify_all_report_elements(self._get_nutrition_report_data())
        )

        return table

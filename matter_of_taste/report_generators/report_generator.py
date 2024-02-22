from abc import ABC, abstractmethod

from matter_of_taste.models.nutrition_report import NutritionReport


class ReportGenerator(ABC):
    def __init__(self, nutrition_report: NutritionReport) -> None:
        self.nutrition_report = nutrition_report

    @abstractmethod
    def generate(self) -> None:
        ...

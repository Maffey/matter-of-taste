import os

import dacite
import requests
from dotenv import load_dotenv, find_dotenv
from requests import Response

from matter_of_taste.models.nutrition_result import NutritionInformation

load_dotenv(find_dotenv())


class CaloriesCalculator:
    _API_NINJAS_KEY: str = os.getenv("API_NINJAS_KEY")
    _API_URL: str = "https://api.api-ninjas.com/v1/nutrition?query={}"
    _API_HEADERS: dict[str, str] = {"X-Api-Key": _API_NINJAS_KEY}
    _ERROR_NUTRITION_INFORMATION = "ERROR"

    @classmethod
    def get_nutrition_information(cls, query: str) -> list[NutritionInformation]:
        response = requests.get(cls._API_URL.format(query), headers=cls._API_HEADERS)
        if response.status_code == requests.codes.ok:
            return cls._process_nutrition(response)
        else:
            print("Error:", response.status_code, response.text)
            return []

    @staticmethod
    def _process_nutrition(response: Response) -> list[NutritionInformation]:
        ingredients = response.json()
        return [
            dacite.from_dict(NutritionInformation, nutrition)
            for nutrition in ingredients
        ]


if __name__ == "__main__":
    nutrition_info = CaloriesCalculator.get_nutrition_information(
        "chicken, beef and water"
    )
    print(nutrition_info)

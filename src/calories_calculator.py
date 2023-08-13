import os

import requests
from dotenv import load_dotenv, find_dotenv

# TODO https://api-ninjas.com/api/nutrition
#  If this works smoothly, NLP can be ditched, as this uses it anyway.

load_dotenv(find_dotenv())


class CaloriesCalculator:
    _API_NINJAS_KEY: str = os.getenv("API_NINJAS_KEY")
    _API_URL: str = "https://api.api-ninjas.com/v1/nutrition?query={}"
    _API_HEADERS: dict[str, str] = {"X-Api-Key": _API_NINJAS_KEY}
    _ERROR_NUTRITION_INFORMATION = "ERROR"

    @classmethod
    def get_nutrition_information(cls, query: str) -> str:
        response = requests.get(cls._API_URL.format(query), headers=cls._API_HEADERS)
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            print("Error:", response.status_code, response.text)
            return cls._ERROR_NUTRITION_INFORMATION


if __name__ == "__main__":
    nutrition_info = CaloriesCalculator.get_nutrition_information("banana")
    print(nutrition_info)
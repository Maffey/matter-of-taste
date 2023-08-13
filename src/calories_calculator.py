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

    def get_nutrition_information(self, query: str) -> str:
        response = requests.get(self._API_URL.format(query), headers=self._API_HEADERS)
        if response.status_code == requests.codes.ok:
            return response.text
        else:
            print("Error:", response.status_code, response.text)
            return "Error while trying to fetch nutrition information."

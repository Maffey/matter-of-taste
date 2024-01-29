import logging
import re
import time
from typing import Optional

from src.recipe_components.calories_calculator import CaloriesCalculator
from src.models.nutrition_report import NutritionReport
from src.models.nutrition_result import NutritionInformation, get_empty_nutrition_result
from src.models.recipe import TokenizedRecipe
from src.models.servings import ServingsStrategy
from src.recipe_components.recipe_scraper import RecipeScraper
from src.recipe_components.recipe_translator import (
    translate_recipe_to_english,
    tokenize_recipe,
)

process_logger = logging.getLogger(__name__)

_API_CALLS_DELAY = 0.1

_NUMBER_REGEX = r"\d+"
_RANGE_OF_NUMBERS_REGEX = r"(\d+)\s*[-–]\s*(\d+)"


class TooManyNumbersDetectedException(Exception):
    def __init__(self):
        super().__init__(
            "Too many numbers detected in the servings field. "
            "Cannot find which one means what."
        )


def prepare_nutrition_report(
    url: str, servings_strategy: ServingsStrategy
) -> NutritionReport:
    process_logger.info("Preparing nutrition report...")
    title, recipe = extract_recipe_data_from_url(url)
    servings, nutrition_summary, nutrition_data = get_nutrition_data(
        recipe, servings_strategy
    )
    process_logger.debug(f"{nutrition_data=}")
    process_logger.info("Report is finished.")
    return NutritionReport(
        recipe_name=title,
        url=url,
        servings=servings,
        summary=nutrition_summary,
        ingredients=nutrition_data,
    )


def extract_recipe_data_from_url(url: str) -> tuple[str, TokenizedRecipe]:
    process_logger.info("Scrapping the recipe...")
    scraper = RecipeScraper(url)
    scrapped_title = scraper.get_recipe_title()
    scrapped_recipe = scraper.get_recipe()
    process_logger.debug(scrapped_recipe)
    process_logger.info("Translating and tokenizing...")
    translated_recipe = translate_recipe_to_english(scrapped_recipe)
    return scrapped_title, tokenize_recipe(translated_recipe)


def get_nutrition_data(
    tokenized_recipe: TokenizedRecipe, servings_strategy: ServingsStrategy
) -> tuple[Optional[int], NutritionInformation, list[NutritionInformation]]:
    all_nutrition_information: list[NutritionInformation] = []
    summarized_nutrition_info: NutritionInformation = get_empty_nutrition_result(
        "Summary"
    )
    process_logger.info("Gathering nutrition information...")
    for ingredient in tokenized_recipe.ingredients:
        nutrition_info_of_single_bullet_in_list = (
            CaloriesCalculator.get_nutrition_information(ingredient)
        )
        process_logger.debug(nutrition_info_of_single_bullet_in_list)

        for nutrition_info in nutrition_info_of_single_bullet_in_list:
            summarized_nutrition_info += nutrition_info
            all_nutrition_information.append(nutrition_info)

        time.sleep(_API_CALLS_DELAY)

    servings = (
        _convert_servings_to_number(tokenized_recipe.servings, servings_strategy)
        if tokenized_recipe.servings
        else None
    )
    return servings, summarized_nutrition_info, all_nutrition_information


def _convert_servings_to_number(
    tokenized_servings: str, servings_strategy: ServingsStrategy
) -> int:
    found_numbers = re.findall(_NUMBER_REGEX, tokenized_servings)
    match len(found_numbers):
        case 1:
            return int(found_numbers[0])
        case 2:
            numbers_range = re.search(_RANGE_OF_NUMBERS_REGEX, tokenized_servings)
            if numbers_range:
                fewer_portions, more_portions = (
                    int(number) for number in numbers_range.groups()
                )
                return (
                    fewer_portions
                    if servings_strategy is ServingsStrategy.FEWER_SERVINGS
                    else more_portions
                )
        case _:
            raise TooManyNumbersDetectedException

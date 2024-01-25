import logging
import re
import time

from src.calories_calculator import CaloriesCalculator
from src.control_flow import TooManyNumbersDetectedException
from src.models.nutrition_report import NutritionReport
from src.models.nutrition_result import NutritionInformation, get_empty_nutrition_result
from src.models.recipe import TokenizedRecipe
from src.recipe_scraper import RecipeScraper
from src.recipe_translator import translate_recipe_to_english, tokenize_recipe

_API_CALLS_DELAY = 0.1

logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(name)s : %(message)s",
)
main_logger = logging.getLogger(__name__)


# TODO move those functions out of main
def _extract_recipe_data_from_url(url: str) -> TokenizedRecipe:
    main_logger.info("Scrapping the recipe...")
    scraper = RecipeScraper(url)
    scrapped_recipe = scraper.get_recipe()
    main_logger.debug(scrapped_recipe)
    main_logger.info("Translating and tokenizing...")
    translated_recipe = translate_recipe_to_english(scrapped_recipe)
    return tokenize_recipe(translated_recipe)


def _get_nutrition_data(
    tokenized_recipe: TokenizedRecipe,
) -> tuple[int, NutritionInformation, list[NutritionInformation]]:
    all_nutrition_information: list[NutritionInformation] = []
    summarized_nutrition_info: NutritionInformation = get_empty_nutrition_result(
        "Summary"
    )
    main_logger.info("Gathering nutrition information...")
    for ingredient in tokenized_recipe.ingredients:
        nutrition_info_of_single_bullet_in_list = (
            CaloriesCalculator.get_nutrition_information(ingredient)
        )
        main_logger.debug(nutrition_info_of_single_bullet_in_list)

        for nutrition_info in nutrition_info_of_single_bullet_in_list:
            summarized_nutrition_info += nutrition_info
            all_nutrition_information.append(nutrition_info)

        time.sleep(_API_CALLS_DELAY)

    servings = _convert_servings_to_number(tokenized_recipe.servings)
    return servings, summarized_nutrition_info, all_nutrition_information


def _convert_servings_to_number(tokenized_servings: str) -> int:
    found_numbers = re.findall(r"\d+", tokenized_servings)
    if found_numbers and len(found_numbers) == 1:
        return int(found_numbers[0])
    raise TooManyNumbersDetectedException


def main():
    # url = "https://www.kwestiasmaku.com/dania_dla_dwojga/kanapki/kanapka_klubowa/przepis.html"
    # url = "https://www.kwestiasmaku.com/kuchnia_polska/rosol/przepis.html"
    url = "https://www.kwestiasmaku.com/zielony_srodek/marchewka/makaron_ryzowy_marchewka_tofu/przepis.html"
    tokenized_recipe = _extract_recipe_data_from_url(url)
    servings, nutrition_summary, nutrition_data = _get_nutrition_data(tokenized_recipe)
    main_logger.debug(f"{nutrition_data=}")

    main_logger.info("Preparing nutrition report...")
    # TODO extract recipe name
    report = NutritionReport(
        recipe_name="",
        url=url,
        servings=servings,
        summary=nutrition_summary,
        ingredients=nutrition_data,
    )
    main_logger.info("Report is finished.")
    print(report)


if __name__ == "__main__":
    main()

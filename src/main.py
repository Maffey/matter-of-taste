import time

from src.calories_calculator import CaloriesCalculator
from src.recipe_scraper import RecipeScraper
from src.recipe_translator import translate_recipe_to_english, tokenize_recipe


def main():
    url = "https://www.kwestiasmaku.com/dania_dla_dwojga/kanapki/kanapka_klubowa/przepis.html"
    scraper = RecipeScraper(url)
    scrapped_recipe = scraper.get_recipe()
    print(scrapped_recipe)
    translated_recipe = translate_recipe_to_english(scrapped_recipe)
    tokenized_recipe = tokenize_recipe(translated_recipe)
    # TODO merge tokens somehow
    for ingredient in tokenized_recipe.ingredients:
        ingredient = " ".join(ingredient)
        nutrition_info = CaloriesCalculator.get_nutrition_information(ingredient)
        print(nutrition_info)
        time.sleep(0.5)  # just to not harass API for now

    print("Finished.")


if __name__ == "__main__":
    main()

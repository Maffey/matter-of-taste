import logging

import typer

from src.models.servings import ServingsStrategy
from src.recipe_components.data_gathering import prepare_nutrition_report

logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(name)s : %(message)s",
)
main_logger = logging.getLogger(__name__)


def main(url: str, more_servings: bool = False) -> None:
    # TODO ship it as standalone script somehow
    # url = "https://www.kwestiasmaku.com/dania_dla_dwojga/kanapki/kanapka_klubowa/przepis.html"
    # url = "https://www.kwestiasmaku.com/kuchnia_polska/rosol/przepis.html"
    # url = "https://www.kwestiasmaku.com/zielony_srodek/marchewka/makaron_ryzowy_marchewka_tofu/przepis.html"
    # url = "https://www.kwestiasmaku.com/pasta/lasagne_bolognese/przepis.html"

    if more_servings:
        report = prepare_nutrition_report(url, ServingsStrategy.MORE_SERVINGS)
    else:
        report = prepare_nutrition_report(url, ServingsStrategy.FEWER_SERVINGS)

    print(report)


if __name__ == "__main__":
    typer.run(main)

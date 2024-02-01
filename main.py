import logging

import typer
from rich import print
from typing_extensions import Annotated

from matter_of_taste.models.servings import ServingsStrategy
from matter_of_taste.recipe_components.data_gathering import prepare_nutrition_report
from matter_of_taste.user_interface.arguments_parsing import (
    _validate_matter_of_taste_url_regex,
)

logging.basicConfig(
    encoding="utf-8",
    level=logging.INFO,
    format="%(asctime)s [%(levelname)s] - %(name)s : %(message)s",
)
main_logger = logging.getLogger(__name__)


def main(
    url: Annotated[
        str,
        typer.Argument(
            callback=_validate_matter_of_taste_url_regex,
            help="URL of the recipe on Kwestia Smaku.",
        ),
    ],
    more_servings: Annotated[
        bool,
        typer.Option(
            help="Request more servings of the recipe, "
            "if the recipe contains a range of servings. "
            "By default, fewer servings are requested."
        ),
    ] = False,
) -> None:
    """
    Run matter-of-taste.
    Matter-of-taste scraps recipe from Kwestia Smaku website
    and calculates calories and other nutrition information for the whole recipe.
    """
    # TODO ship it as standalone script somehow
    # url = "https://www.kwestiasmaku.com/dania_dla_dwojga/kanapki/kanapka_klubowa/przepis.html"
    # url = "https://www.kwestiasmaku.com/kuchnia_polska/rosol/przepis.html"
    # url = "https://www.kwestiasmaku.com/zielony_srodek/marchewka/makaron_ryzowy_marchewka_tofu/przepis.html"
    # url = "https://www.kwestiasmaku.com/pasta/lasagne_bolognese/przepis.html"

    if more_servings:
        report = prepare_nutrition_report(url, ServingsStrategy.MORE_SERVINGS)
    else:
        report = prepare_nutrition_report(url, ServingsStrategy.FEWER_SERVINGS)

    print(f"[blue]{report}[/blue]")


if __name__ == "__main__":
    typer.run(main)

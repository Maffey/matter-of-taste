import re
from argparse import ArgumentParser, ArgumentTypeError
from dataclasses import dataclass

from src.models.servings import ServingsStrategy

_MATTER_OF_TEST_URL_REGEX = re.compile(
    "^https?:\\/\\/(?:www\\.)?[-a-zA-Z0-9@:%._\\+~#=]{1,256}\\.[a-zA-Z0-9()]{1,6}\\b(?:[-a-zA-Z0-9()@:%_\\+.~#?&\\/=]*)$"
)


@dataclass
class Arguments:
    url: str
    servings_strategy: ServingsStrategy = ServingsStrategy.FEWER_SERVINGS


def get_arguments() -> Arguments:
    arguments = _get_configured_parser().parse_args()
    if arguments.more_servings:
        return Arguments(
            url=arguments.url, servings_strategy=ServingsStrategy.MORE_SERVINGS
        )
    else:
        return Arguments(
            url=arguments.url, servings_strategy=ServingsStrategy.FEWER_SERVINGS
        )


def _get_configured_parser() -> ArgumentParser:
    # TODO migrate to typer
    parser = ArgumentParser()
    parser.add_argument(
        "url",
        type=_matter_of_taste_url_regex,
        help="URL of the recipe on Kwestia Smaku.",
    )
    parser.add_argument(
        "-mp",
        "--more-servings",
        action="store_true",
        help="Request more servings of the recipe, if the recipe contains a range of servings. By default, fewer servings are requested.",
    )
    return parser


def _matter_of_taste_url_regex(url: str):
    if not _MATTER_OF_TEST_URL_REGEX.match(url):
        raise ArgumentTypeError("[ERROR] Not a valid Kwestia Smaku URL.")
    return url

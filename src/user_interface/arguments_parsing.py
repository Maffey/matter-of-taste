import re

import typer

_MATTER_OF_TEST_URL_REGEX = re.compile(
    "^https?://(?:www\\.)kwestiasmaku?[-a-zA-Z0-9@:%._+~#=]{1,256}\\.[a-zA-Z0-9()]{1,"
    "6}\\b[-a-zA-Z0-9()@:%_+.~#?&/=]*$"
)


def _validate_matter_of_taste_url_regex(url: str) -> str:
    if not _MATTER_OF_TEST_URL_REGEX.match(url):
        raise typer.BadParameter("Not a valid Kwestia Smaku URL.")
    return url

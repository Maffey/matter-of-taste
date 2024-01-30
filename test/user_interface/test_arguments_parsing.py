import pytest
import typer

from src.user_interface.arguments_parsing import _validate_matter_of_taste_url_regex


@pytest.mark.parametrize(
    "url",
    (
        "https://www.kwestiasmaku.com/przepis.html",
        "https://www.kwestiasmaku.com/sciezka/przepis.html",
    ),
)
def test_validate_matter_of_taste_url_regex_passes(url):
    _validate_matter_of_taste_url_regex(url)


@pytest.mark.parametrize(
    "url", ("https://www.example.com/przepis.html", "www.cantexist.com")
)
def test_validate_matter_of_taste_url_regex_fails(url):
    with pytest.raises(typer.BadParameter):
        _validate_matter_of_taste_url_regex(url)

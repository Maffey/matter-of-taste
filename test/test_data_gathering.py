import pytest

from src.data_gathering import _convert_servings_to_number
from src.models.servings import ServingsStrategy


@pytest.mark.parametrize(
    "servings_text, expected_servings, servings_strategy",
    [
        ("Serves 4", 4, None),
        ("Serves 6-8", 6, ServingsStrategy.FEWER_SERVINGS),
        ("Serves 6-8", 8, ServingsStrategy.MORE_SERVINGS),
        # TODO case to cover: portions as words?
    ],
)
def test_convert_servings_to_number(
    servings_text, expected_servings, servings_strategy
):
    assert (
        _convert_servings_to_number(servings_text, servings_strategy)
        == expected_servings
    )
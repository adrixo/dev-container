from api.functions.functions import sum
import pytest

@pytest.mark.unit
def test_sum_of_two_positive_numbers():
    assert sum(1, 2) == 3

@pytest.mark.unit
def test_sum_of_two_negative_numbers():
    assert sum(-1, -2) == -3
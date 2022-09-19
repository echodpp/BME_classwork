from blood_calculator import *
import pytest


@pytest.mark.parametrize(
    "input,expected",
    [(65, "Normal"), (50, "Borderline Low"), (45, "Borderline Low"), (35, "Low")],
)
def test_check_HDL(input, expected):
    answer = check_HDL(input)
    assert answer == expected


def test_check_LDL():
    answer = check_LDL(180)
    assert answer == "High"

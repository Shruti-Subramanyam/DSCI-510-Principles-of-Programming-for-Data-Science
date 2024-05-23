import glob
import importlib
import pytest


try:
    script_path = glob.glob("./lab3.py")[0]
    module_path = script_path[2:-3]
    module = importlib.import_module(module_path)
except BaseException:
    raise Exception(
        "No script is available. Please follow the assignment instructions."
    )

try:
    sum_of_squares_of_digits = module.sum_of_squares_of_digits
    is_happy_number = module.is_happy_number
    is_acceptable = module.is_acceptable

except BaseException:
    raise Exception(
        "Please ensure all required functions have been implemented.")


@pytest.mark.parametrize('num, ans', [
    (123, 14),
    (987, 194),
    (0, 0),
    (-45, "Exception")
])
def test_sum_of_squares_of_digits(num, ans):
    if ans == "Exception":
        with pytest.raises(Exception):
            sum_of_squares_of_digits(num)
    else:
        assert sum_of_squares_of_digits(num) == ans


@pytest.mark.parametrize('num, ans', [
    (19, True),
    (2, False),
    (-45, "Exception")
])
def test_is_happy_number(num, ans):
    if ans == "Exception":
        with pytest.raises(Exception):
            is_happy_number(num)
    else:
        assert is_happy_number(num) == ans


@pytest.mark.parametrize('password, ans', [
    ("Pass*!123", False),
    ("Good*password!123", True),
    ("don’t try stealing my password", False)
])
def test_is_acceptable(password, ans):
    assert is_acceptable(password) == ans

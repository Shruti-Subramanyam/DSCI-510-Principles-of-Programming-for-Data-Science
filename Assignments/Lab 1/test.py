# DO NOT CHANGE THE CONTENTS OF THIS FILE; these are tests to ensure your functions are correctly implemented.
# Pytest needs to be installed in your environment.
import pytest

try:
    import glob
    import importlib
    script_path = glob.glob('./lab1.py')[0]
    module_path = script_path[2:-3]
    module = importlib.import_module(module_path)
except:
    raise Exception(
        'No script is available. Please follow the assignment instructions.')

try:
    degrees_to_radians = module.degrees_to_radians
    vowel_count = module.vowel_count
    triangle_hypotenuse = module.triangle_hypotenuse
except:
    raise Exception(
        'Please ensure all required functions have been implemented.')


@pytest.mark.parametrize('degree, radian', [
    (1, 0.017),
    (108, 1.885),
    (0, 0)
])
def test_degrees_to_radians(degree, radian):
    assert pytest.approx(degrees_to_radians(degree), abs=1e-3) == radian


@pytest.mark.parametrize('s, count', [
    ('sentence', 3),
    ('aeiou', 5),
    ('', 0)
])
def test_vowel_count(s, count):
    assert vowel_count(s) == count


@pytest.mark.parametrize('base, height, result', [
    (3, 4, 5),
    (1, 1, 1.414),
    (0, 0, 0)
])
def test_triangle_hypotenuse(base, height, result):
    assert pytest.approx(triangle_hypotenuse(base, height), abs=1e-3) == result

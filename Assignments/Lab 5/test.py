import glob
import importlib

import pytest

try:
    script_path = glob.glob("./lab5.py")[0]
    module_path = script_path[2:-3]
    module = importlib.import_module(module_path)
except BaseException:
    raise Exception(
        "No script is available. Please follow the assignment instructions."
    )

try:
    analyse_student_data = module.analyse_student_data
    analyse_bank_data = module.analyse_bank_data

except BaseException:
    raise Exception("Please ensure all required functions have been implemented.")


@pytest.mark.parametrize(
    "filename,ans",
    [
        (
            "student_performance.csv",
            (
                870,
                {"Male": 439, "Female": 431},
                {"Track C": 76.58, "Track B": 74.21, "Track A": 73.26},
                "Associate's Degree",
                74.18,
                [
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                ],
            ),
        ),
        (
            "student_performance_1.csv",
            (
                1000,
                {"Male": 469, "Female": 531},
                {"Track C": 74.82, "Track A": 74.47, "Track B": 73.4},
                "Bachelor's Degree",
                74.87,
                [
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Female"),
                    (99, "Male"),
                    (99, "Female"),
                ],
            ),
        ),
        (
            "student_performance_2.csv",
            (
                100,
                {"Male": 43, "Female": 57},
                {"Track A": 80.14, "Track B": 75.03, "Track C": 74.15},
                "Associate's Degree",
                76.08,
                [(99, "Female"), (99, "Male"), (99, "Male")],
            ),
        ),
        (
            "student_performance_3.csv",
            (
                4,
                {"Male": 3, "Female": 1},
                {"Track A": 75.0, "Track B": 88.0, "Track C": 60.0},
                "Associate's Degree",
                81.5,
                [(85, "Female"), (85, "Male")],
            ),
        ),
        (
            "student_performance_4.csv",
            (
                4,
                {"Male": 3, "Female": 1},
                {"Track B": 83.67, "Track C": 60.0},
                "Associate's Degree",
                81.5,
                [(85, "Female"), (85, "Male")],
            ),
        ),
    ],
)
def test_analyse_student_data(filename, ans):
    assert analyse_student_data(filename) == ans


@pytest.mark.parametrize(
    "filename,ans",
    [
        ("bank_transactions.csv", (297.65, 2, 8578.79)),
        ("bank_transactions_1.csv", (1963.97, 23, 39607.43)),
        ("bank_transactions_2.csv", (1814.31, 10, -4042.5)),
    ],
)
def test_analyse_bank_data(filename, ans):
    assert analyse_bank_data(filename) == ans

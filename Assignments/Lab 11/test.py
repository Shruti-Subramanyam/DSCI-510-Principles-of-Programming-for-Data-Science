import pytest

try:
    import glob
    import importlib
    import numpy as np

    script_path = glob.glob("./lab11.py")[0]
    module_path = script_path[2:-3]
    module = importlib.import_module(module_path)
except Exception:
    raise Exception(
        "No script is available. Please follow the assignment instructions."
    )

try:
    LinearAlgebra = module.LinearAlgebra
    analyze_sales = module.analyze_sales
except Exception:
    raise Exception("Please ensure all required classes have been implemented.")


@pytest.mark.parametrize(
    "array_1, array_2, inverse",
    [
        (
            np.array([[2, 3], [1, 4]]),
            np.array([[5, 6], [3, 8]]),
            np.array([[0.06944444, -0.05902778], [-0.05902778, 0.05642361]]),
        ),
        (
            np.array([[1, 2], [3, 4]]),
            np.array([[5, 6], [7, 8]]),
            np.array([[3.8125, -2.4375], [-2.4375, 1.5625]]),
        ),
    ],
)
def test_linear_algebra(array_1, array_2, inverse):
    linalg = LinearAlgebra()
    obtained_inverse = linalg.perform_operations(array_1, array_2)
    assert np.allclose(obtained_inverse, inverse)


def test_linear_algebra_exception():
    with pytest.raises(Exception):
        linalg = LinearAlgebra()
        array_1 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        array_2 = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
        linalg.perform_operations(array_1, array_2)


@pytest.mark.parametrize(
    "file_name,ans",
    [
        (
            "test1.csv",
            {
                "top_product": "R",
                "top_month": "December",
                "average_sales_per_product": {
                    "A": 199.0,
                    "B": 245.0,
                    "D": 395.0,
                    "G": 317.0,
                    "N": 66.0,
                    "R": 408.5,
                    "U": 169.0,
                    "Z": 475.0,
                },
            },
        ),
        (
            "test2.csv",
            {
                "top_product": "I",
                "top_month": "June",
                "average_sales_per_product": {
                    "A": 240.0,
                    "D": 215.0,
                    "E": 340.33,
                    "H": 151.0,
                    "I": 321.5,
                    "K": 304.0,
                    "L": 352.0,
                    "N": 315.0,
                    "P": 355.0,
                    "Q": 51.0,
                    "R": 279.0,
                    "T": 269.0,
                    "U": 35.0,
                    "V": 369.0,
                    "Y": 359.0,
                },
            },
        ),
        (
            "test3.csv",
            {
                "top_product": "P",
                "top_month": "May",
                "average_sales_per_product": {
                    "A": 248.75,
                    "B": 127.5,
                    "C": 355.0,
                    "D": 279.57,
                    "E": 449.0,
                    "F": 49.0,
                    "G": 242.0,
                    "H": 279.67,
                    "I": 239.33,
                    "J": 143.75,
                    "K": 234.6,
                    "L": 187.25,
                    "M": 70.33,
                    "N": 276.86,
                    "O": 175.5,
                    "P": 307.43,
                    "Q": 477.0,
                    "R": 166.0,
                    "S": 280.5,
                    "T": 241.67,
                    "V": 254.5,
                    "W": 318.0,
                    "X": 224.83,
                    "Y": 161.5,
                    "Z": 320.0,
                },
            },
        ),
    ],
)
def test_analyze_sales(file_name, ans):
    assert analyze_sales(file_name) == ans

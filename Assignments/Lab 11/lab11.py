from typing import Dict, Union
import numpy as np
import pandas as pd


class LinearAlgebra:
    def matrix_addition(self, array_1: np.ndarray, array_2: np.ndarray) -> np.ndarray:
        if not isinstance(array_1, np.ndarray) or not isinstance(array_2, np.ndarray):
            raise Exception("Please input Numpy arrays")
        if not array_1.shape == array_2.shape and array_1.shape[0] == array_2.shape[1]:
            raise Exception("Please input matrices of same shape and square size")
        return np.add(array_1, array_2)

    def matrix_multiplication(
        self, array_1: np.ndarray, array_2: np.ndarray
    ) -> np.ndarray:
        if not isinstance(array_1, np.ndarray) or not isinstance(array_2, np.ndarray):
            raise Exception("Please input Numpy arrays")
        if not array_1.shape == array_2.shape and array_1.shape[0] == array_2.shape[1]:
            raise Exception("Please input matrices of same shape and square size")
        return np.dot(array_1, array_2)

    def matrix_transposition(self, array: np.ndarray) -> np.ndarray:
        if not isinstance(array, np.ndarray):
            raise Exception("Please input Numpy arrays")
        if not array.shape[0] == array.shape[1]:
            raise Exception("Please input matrices of square size")
        return np.transpose(array)

    def matrix_determinant(self, array: np.ndarray) -> float:
        if not isinstance(array, np.ndarray):
            raise Exception("Please input Numpy arrays")
        if not array.shape[0] == array.shape[1]:
            raise Exception("Please input matrices of square size")
        return np.linalg.det(array)

    def matrix_inversion(self, array: np.ndarray) -> np.ndarray:
        if not isinstance(array, np.ndarray):
            raise Exception("Please input Numpy arrays")
        if not array.shape[0] == array.shape[1]:
            raise Exception("Please input matrices of square size")
        if self.matrix_determinant(array) == 0:
            raise Exception("Inversion operation cannot be performed")
        return np.linalg.inv(array)

    def perform_operations(self, array_1: np.ndarray, array_2: np.ndarray):
        if not isinstance(array_1, np.ndarray) or not isinstance(array_2, np.ndarray):
            raise Exception("Please input Numpy arrays")
        if not array_1.shape == array_2.shape and array_1.shape[0] == array_2.shape[1]:
            raise Exception("Please input matrices of same shape and square size")
        output1 = self.matrix_addition(array_1, array_2)
        output2 = self.matrix_addition(
            self.matrix_transposition(array_1), self.matrix_transposition(array_2)
        )
        output3 = self.matrix_multiplication(output1, output2)
        if self.matrix_determinant(output3) == 0:
            raise Exception("Inversion operation cannot be performed")
        return self.matrix_inversion(output3)


def analyze_sales(file_name: str) -> Dict[str, Union[int, str]]:
    df = pd.read_csv(file_name)
    prod_high_sales = df.groupby("Product")["Sales"].sum()
    top_product = prod_high_sales.idxmax()
    month_high_sales = df.groupby("Month")["Sales"].sum()
    top_month = month_high_sales[month_high_sales == month_high_sales.max()].index
    top_month = sorted(top_month)[0]
    average_sales_per_product = df.groupby("Product")["Sales"].mean().round(2).to_dict()
    final_result = {
        "top_product": top_product,
        "top_month": top_month,
        "average_sales_per_product": average_sales_per_product,
    }
    return final_result

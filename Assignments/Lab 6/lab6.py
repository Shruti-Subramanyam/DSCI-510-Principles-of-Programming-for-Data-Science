class MyStack:
    def __init__(self):
        self.elements = []

    def __str__(self) -> str:
        if not self.elements:
            return ""
        ele = " -> ".join(map(str, self.elements[::-1]))
        return ele

    def push(self, element: int):
        try:
            if not isinstance(element, int):
                raise Exception("Invalid Input")
            else:
                self.elements.append(element)
        except ValueError:
            raise

    def pop(self) -> int:
        try:
            if not self.elements:
                raise Exception(
                    "The MyStack is empty. No more pop operations can be performed"
                )
            else:
                return self.elements.pop()
        except Exception:
            raise

    def min(self) -> int:
        if not self.elements:
            return None
        return min(self.elements)

    def max(self) -> int:
        if not self.elements:
            return None
        return max(self.elements)

    def is_empty(self) -> bool:
        if not self.elements:
            return True
        else:
            return False


class MyQueue:
    def __init__(self):
        self.elements = []

    def __str__(self) -> str:
        if not self.elements:
            return ""
        ele = " -> ".join(map(str, self.elements))
        return ele

    def push(self, element: int):
        try:
            if not isinstance(element, int):
                raise Exception("Invalid Input")
            else:
                self.elements.append(element)
        except ValueError:
            raise

    def pop(self) -> int:
        try:
            if not self.elements:
                raise Exception(
                    "The MyStack is empty. No more pop operations can be performed"
                )
            else:
                return self.elements.pop(0)
        except Exception:
            raise

    def min(self) -> int:
        if not self.elements:
            return None
        return min(self.elements)

    def max(self) -> int:
        if not self.elements:
            return None
        return max(self.elements)

    def is_empty(self) -> bool:
        if not self.elements:
            return True
        else:
            return False


class Transactions:
    def __init__(self):
        self.transaction_map = {}

    def add_transaction(
        self,
        transaction_id: int,
        transaction_type: str,
        transaction_amount: float,
        transaction_details: str,
    ):
        if transaction_type not in ("deposit", "withdrawal"):
            raise ValueError("Invalid transaction type")

        if transaction_id in self.transaction_map:
            raise ValueError("ID already exists")

        transaction_details = {
            "transaction_type": transaction_type,
            "transaction_amount": transaction_amount,
            "transaction_details": transaction_details,
        }
        self.transaction_map[transaction_id] = transaction_details

    def get_transaction(self, transaction_id: int) -> dict:
        if transaction_id in self.transaction_map:
            return self.transaction_map[transaction_id]
        else:
            return {}

    def get_all_transactions(self) -> dict:
        return self.transaction_map

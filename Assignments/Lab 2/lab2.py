from typing import List, Tuple


def format_date(day: int, month: int, year: int) -> str:
    try:
        if month < 1 or month > 12 or day < 1 or day > 31:
            raise Exception(f"The given date: {day}, {month}, {year} is invalid")
        if month == 2:
            if day > 29 or ((day > 28) and not (year % 4 == 0 and (year % 100 != 0 or year % 400 == 0))):
                raise Exception(f"The given date: {day}, {month}, {year} is invalid")
        day = str(day).zfill(2)
        mon_name = {1: "January", 2: "February", 3: "March", 4: "April", 5: "May", 6: "June", 7: "July", 8: "August", 9: "September", 10: "October", 11: "November", 12: "December"}
        date = f"{day} {mon_name[month]}, {year}"
        return date
    except Exception as e:
        raise e


def split_by_delimiter(some_string: str, delimiter: str) -> list:
    try:
        output = list()
        string = str()
        if isinstance(some_string, str) and isinstance(delimiter, str):
            for character in some_string:
                if character is not delimiter:
                    string = string + character
                else:
                    output.append(string)
                    string = ''
            output.append(string)
            return output
        else:
            raise ValueError("Invalid Input")
    except ValueError:
        raise


def check_perfect_squares(tups: List[Tuple]) -> bool:
    # Lab 2 Assignment function 3
    try:
        for pair in tups:
            if isinstance(pair, Tuple) and len(pair) == 2 and isinstance(pair[0], int) and isinstance(pair[1], int):
                if pair[0] * pair[0] != pair[1]:
                    return False
            else:
                raise ValueError("Invalid Input")
        return True
    except ValueError:
        raise

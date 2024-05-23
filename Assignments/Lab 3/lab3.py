import string


def sum_of_squares_of_digits(num: int) -> int:
    """
    This function returns the sum of squares of the individual digits
    of a provided number
    """
    try:
        if isinstance(num, int) or num >= 0:
            total = 0
            temp = str(num)
            for i in temp:
                total += int(i) * int(i)
            return total
        else:
            raise ValueError()
    except Exception:
        raise Exception("Invalid input")


def is_happy_number(num: int) -> bool:
    # This code returns boolean value if a digit is happy number
    try:
        lst = set()
        while num != 1:
            num = sum_of_squares_of_digits(num)
            if num in lst:
                return False
            else:
                lst.add(num)
                print(lst)
        return True
    except Exception:
        raise Exception("Invalid input")


def is_acceptable(password: str) -> bool:
    # This code returns the boolean value for password acceptance
    try:
        if len(password) < 10 or len(password) > 20:
            return False
        empty_space = 0
        check_lower = 0
        check_upper = 0
        special_ch = 0
        digits = 0
        for i in password:
            if i == "\t" or i == "\n":
                return False
            elif i.islower():
                check_lower += 1
            elif i.isupper():
                check_upper += 1
            elif i.isspace():
                empty_space += 1
            elif i.isdigit():
                digits += 1
            elif i in string.punctuation:
                special_ch += 1
            else:
                return False
        if check_lower >= 1 and check_upper >= 1 and digits >= 2 and special_ch >= 2:
            return True
        else:
            return False
    except Exception:
        raise Exception("Invalid input")

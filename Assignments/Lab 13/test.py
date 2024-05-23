import pytest

try:
    import glob
    import importlib

    script_path = glob.glob("./lab13.py")[0]
    module_path = script_path[2:-3]
    module = importlib.import_module(module_path)
except Exception:
    raise Exception(
        "No script is available. Please follow the assignment instructions."
    )

try:
    email_parser = module.email_parser
    analyze_employee_data = module.analyze_employee_data
except Exception:
    raise Exception("Please ensure all required classes have been implemented.")


@pytest.mark.parametrize(
    "filepath, domains_to_parse, result",
    [
        (
            "sample_text.txt",
            ["usc.edu", "isi.edu"],
            {
                "usc.edu": [
                    "support@cs.usc.edu",
                    "support@eng.usc.edu",
                    "support@usc.edu",
                ],
                "isi.edu": ["support@isi.edu", "support@usc.isi.edu"],
            },
        ),
        (
            "sample_text_duplicate.txt",
            ["usc.edu", "isi.edu", "gmail.com"],
            {
                "usc.edu": ["john@usc.edu"],
                "isi.edu": ["mary.smith@isi.edu"],
                "gmail.com": [],
            },
        ),
        (
            "sample_text1.txt",
            ["usc.edu", "isi.edu", "gmail.com"],
            {
                "usc.edu": ["john.doe123@eng.usc.edu", "support@usc.edu"],
                "isi.edu": ["mary.smith@isi.edu"],
                "gmail.com": [],
            },
        ),
    ],
)
def test_email_parser(filepath, domains_to_parse, result):
    assert email_parser(filepath, domains_to_parse) == result


def test_email_parser_exception():
    with pytest.raises(Exception):
        email_parser(
            "sample_text_non_existent.txt",
            ["usc.edu", "isi.edu", "gmail.com", "yahoo.com"],
        )
        email_parser("sample_text.txt", [])
        email_parser("sample_text.txt", "any")
        email_parser("sample_text.txt", 1)


@pytest.mark.parametrize(
    "filepath, threshold, result",
    [
        (
            "employees.db",
            50000.0,
            {
                "average_salary": 55500.00,
                "department_employee_count": {"HR": 2, "IT": 1, "Finance": 1},
            },
        ),
    ],
)
def test_analyze_employee_data(filepath, threshold, result):
    assert analyze_employee_data(filepath, threshold) == result


def test_analyze_employee_data_exception():
    with pytest.raises(Exception):
        analyze_employee_data("employees_non_existent.db", 50000.0)

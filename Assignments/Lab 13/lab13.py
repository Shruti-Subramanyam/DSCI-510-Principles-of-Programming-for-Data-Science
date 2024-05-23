import re
import sqlite3
from typing import List


def email_parser(filepath: str, root_domains: List[str]) -> dict:
    if not isinstance(root_domains, list) or not root_domains:
        raise Exception(
            "Invalid domains_to_parse argument. It should be a list of domains."
        )
    try:
        with open(filepath, "r", encoding="utf-8") as file:
            text = file.read()
    except FileNotFoundError:
        raise Exception("Invalid filepath. The specified file does not exist.")
    parsed_emails = {}
    for domain in root_domains:
        domain_pattern = re.compile(rf"(?i)\b[\w.-]+@[\w.]*{re.escape(domain)}\b")
        matches = set(re.findall(domain_pattern, text))
        valid_emails = sorted(
            filter(lambda x: validate_email_domain(x, domain), matches), key=str.lower
        )
        parsed_emails[domain] = valid_emails
    return parsed_emails


def validate_email(email: str) -> bool:
    email_pattern = re.compile(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Za-z]{2,}\b")
    return bool(re.match(email_pattern, email))


def validate_email_domain(email: str, domain: str) -> bool:
    domain_pattern = re.compile(rf"(?i)\b[\w.-]+@[\w.]*{re.escape(domain)}\b")
    return bool(re.match(domain_pattern, email))


def analyze_employee_data(filepath: str, threshold: float) -> dict:
    try:
        conn = sqlite3.connect(filepath)
    except sqlite3.Error:
        raise Exception("Invalid filepath. The specified file does not exist.")
    cursor = conn.cursor()
    cursor.execute(
        "SELECT department, salary FROM employee_data WHERE salary > ?", (threshold,)
    )
    rows = cursor.fetchall()
    conn.close()
    if not rows:
        return {"average_salary": 0.0, "department_employee_count": {}}
    total_salary = sum(row[1] for row in rows)
    average_salary = round(total_salary / len(rows), 2)
    department_employee_count = {"HR": 0, "IT": 0, "Finance": 0}
    for row in rows:
        department = row[0]
        if department in department_employee_count:
            department_employee_count[department] += 1
    result = {
        "average_salary": average_salary,
        "department_employee_count": department_employee_count,
    }
    return result

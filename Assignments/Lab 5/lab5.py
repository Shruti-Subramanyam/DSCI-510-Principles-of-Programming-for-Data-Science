from typing import List, Tuple
import csv


ASSOCIATE = "Associate's Degree"
HIGH_SCHOOL = "High School"
BACHELOR = "Bachelor's Degree"


def analyse_student_data(
    filename: str,
) -> Tuple[int, dict, dict, str, float, List[Tuple[float, str]]]:
    total_students = int(0)
    male_count = int(0)
    female_count = int(0)
    track_a_count = int(0)
    track_b_count = int(0)
    track_c_count = int(0)
    track_a_sum = float(0)
    track_b_sum = float(0)
    track_c_sum = float(0)
    parental_education = dict(
        {
            ASSOCIATE: int(0),
            HIGH_SCHOOL: int(0),
            BACHELOR: int(0),
        }
    )
    average_reading_score = float(0)
    writing_scores_with_gender = list()

    with open(filename, "r") as csvfile:
        file = csv.DictReader(csvfile)
        for row in file:
            math_score = float(row["MathScore"])
            reading_score = float(row["ReadingScore"])
            writing_score = int(row["WritingScore"])
            total_students += 1
            if row["Gender"] == "Male":
                male_count += 1
            if row["Gender"] == "Female":
                female_count += 1
            if row["Track"] == "Track A":
                track_a_sum += math_score
                track_a_count += 1
            if row["Track"] == "Track B":
                track_b_sum += math_score
                track_b_count += 1
            if row["Track"] == "Track C":
                track_c_sum += math_score
                track_c_count += 1
            if row["ParentalEducation"] == HIGH_SCHOOL:
                parental_education[HIGH_SCHOOL] += 1
            if row["ParentalEducation"] == ASSOCIATE:
                parental_education[ASSOCIATE] += 1
            if row["ParentalEducation"] == BACHELOR:
                parental_education[BACHELOR] += 1
            average_reading_score += (
                reading_score - average_reading_score
            ) / total_students
            writing_scores_with_gender.append((writing_score, row["Gender"]))
    # Track averages of Math scores
    average_math_score_by_track = dict()
    if track_a_count:
        average_math_score_by_track["Track A"] = track_a_sum / track_a_count
    if track_b_count:
        average_math_score_by_track["Track B"] = track_b_sum / track_b_count
    if track_c_count:
        average_math_score_by_track["Track C"] = track_c_sum / track_c_count
    for key in average_math_score_by_track:
        average_math_score_by_track[key] = round(average_math_score_by_track[key], 2)
    # Filter list and keep only the highest
    highest_writing_scores_with_gender = [
        tup
        for tup in writing_scores_with_gender
        if tup[0] == max(writing_scores_with_gender)[0]
    ]
    # Round off
    average_reading_score = round(average_reading_score, 2)
    # Create answer tuple
    answer: Tuple[int, dict, dict, str, float, List[Tuple[float, str]]] = (
        total_students,
        dict({"Male": male_count, "Female": female_count}),
        average_math_score_by_track,
        max(parental_education, key=parental_education.get),
        average_reading_score,
        highest_writing_scores_with_gender,
    )
    return answer


def analyse_bank_data(filename: str) -> Tuple[float, int, float]:
    highest_phone_bill = float(0)
    number_of_rent_transactions = int(0)
    balance = float(0)
    with open(filename, "r") as csvfile:
        file = csv.DictReader(csvfile)
        for row in file:
            amount = float(row["Amount"])
            if row["Description"] == "Phone bill" and amount > highest_phone_bill:
                highest_phone_bill = amount
            if row["Description"] == "Rent":
                number_of_rent_transactions += 1
            if row["Type"] == "Deposit":
                balance += amount
            if row["Type"] == "Withdrawal":
                balance -= amount
    answer: Tuple[float, int, float] = (
        round(highest_phone_bill, 2),
        round(number_of_rent_transactions, 2),
        round(balance, 2),
    )
    return answer

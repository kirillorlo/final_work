import pytest
from final_work import Student


@pytest.mark.parametrize("subjects, grade, expected_average", [
    ("Математика", 4, 4),
    ("Математика", 5, 4.5),
    ("История", 4, 4),
    ("История", 5, 4.5),
])
def test_student_average_grade(subjects, grade, expected_average):
    student = Student("Иван Иванов", "subjects.csv")
    student.add_grade(subjects, grade)
    average_grade = student.get_average_grade()
    assert average_grade == expected_average


def test_get_average_test_score():
    student = Student("Иван Иванов", "subjects.csv")
    student.add_test_score("Математика", 80)
    student.add_test_score("Математика", 90)
    student.add_test_score("История", 70)
    average_test_score = student.get_average_test_score("Математика")
    assert average_test_score == 85


def test_add_test_score():
    student = Student("Иван Иванов", "subjects.csv")
    student.add_test_score("Математика", 80)
    student.add_test_score("Математика", 90)
    assert student.subjects["Математика"]["test_scores"] == [80, 90]

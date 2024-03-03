import pytest
from final_work import Student

# @pytest.mark.parametrize("subject, grade, expected_average", [
#     ("Математика", 4, 4),
#     ("Математика", 5, 4.5),
#     ("История", 4, 4),
#     ("История", 5, 4.5),
# ])
# def test_student_average_grade(subject, grade, expected_average):
#     student = Student("Иван Иванов", "subjects.csv")
#     student.add_grade(subject, grade)
#     average_grade = student.get_average_grade()
#     assert average_grade == expected_average

def test_get_average_grade():
    # Создаем экземпляр класса Student для тестирования
    student = Student()

    # Предполагаемые значения
    expected_result_empty = 0
    expected_result = 4.5

    # Тест 1: проверка, если нет оценок вообще
    assert student.get_average_grade() == expected_result_empty

    # Тест 2: добавляем оценки и проверяем средний балл
    student.add_grade("Математика", 4)
    student.add_grade("Математика", 5)
    student.add_grade("Физика", 4)
    student.add_grade("Физика", 5)
    assert student.get_average_grade() == expected_result
    
    # Тест 3: добавляем оценки только по одному предмету
    student.add_grade("Английский", 5)
    student.add_grade("Английский", 5)
    assert student.get_average_grade() == expected_result_empty

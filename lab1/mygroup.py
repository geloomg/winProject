import statistics as stat

groupmates = [
    {
        "name": "Олег",
        "surname": "Гусейнов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [4, 3, 5]
    },
    {
        "name": "Анастасия",
        "surname": "Гольцова",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 4, 4]
    },
    {
        "name": "Владимир",
        "surname": "Зорин",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 5, 5]
    },
{
        "name": "Кирилл",
        "surname": "Колбасов",
        "exams": ["Информатика", "ЭЭиС", "Web"],
        "marks": [3, 3, 5]
    },
    {
        "name": "Кирилл",
        "surname": "Кузнецов",
        "exams": ["История", "АиГ", "КТП"],
        "marks": [4, 3, 4]
    },
    {
        "name": "Игорь",
        "surname": "Тулегенов",
        "exams": ["Философия", "ИС", "КТП"],
        "marks": [5, 4, 5]
    }
]


def filter_by_mark(mark: int, students: list[dict]) -> list[dict]:
    """Функция фильтрации студентов по заданной средней оценке"""
    return list(filter(lambda student: mark < stat.mean(student['marks']), students))


def print_students(students):
    """Функция вывода на экран списка студентов"""
    print('Имя'.ljust(15), 'Фамилия'.ljust(10), 'Экзамены'.ljust(30), 'Оценки'.ljust(20))
    for student in students:
        print(student["name"].ljust(15), student["surname"].ljust(10),
              str(student["exams"]).ljust(30), str(student["marks"]).ljust(20))


if __name__ == '__main__':
    print_students(filter_by_mark(4, groupmates))






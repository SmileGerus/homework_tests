import pytest

courses1 = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors1 = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
     "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев", "Никита Шумский",
     "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков", "Максим Воронцов", "Евгений Грязнов",
     "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
     "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая", "Денис Ежков",
     "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
     "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина", "Азамат Искаков",
     "Роман Гордиенко"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
     "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин", "Михаил Ларченко"]
]

mentors2 = [
    ["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский"],
    ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев"],
    ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин", "Антон Хорошев", "Максим Валиев"]
]


durations1 = [14, 20, 12, 20]
durations2 = [3, 2, 4, 4]
durations3 = [0, 0, 0, 0]
durations4 = [12, 70, 2, 2]


def max_len(courses, mentors, durations):
    courses_list = []
    for course, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": course, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    duration_index = []
    mcount_index = []
    for index, course in enumerate(courses_list):
        duration_index.append([course["duration"], index])
        mcount_index.append([len(course["mentors"]), index])

    duration_index.sort()
    mcount_index.sort()

    indexes_d = []
    indexes_m = []

    for cou, dur in duration_index:
        indexes_d.append(dur)
    for cou, m in mcount_index:
        indexes_m.append(m)

    print("Связь есть" if indexes_m == indexes_d else "Связи нет")
    print(f"Порядок курсов по длительности: {indexes_d}")
    print(f"Порядок курсов по количеству преподавателей: {indexes_m}")

    return [indexes_d, indexes_m]


@pytest.mark.parametrize(
    'durations, expected', (
        [durations1, [2, 0, 1, 3]],
        [durations2, [1, 0, 2, 3]],
        [durations3, [0, 1, 2, 3]],
        [durations4, [2, 3, 0, 1]]
    )
)
def test_courses_by_duration(durations: list, expected: int):
    result = max_len(courses1, mentors1, durations)[0]
    assert result == expected

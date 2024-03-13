import pytest

courses1 = ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]
mentors1 = [["Филипп Воронов", "Анна Юшина", "Иван Бочаров", "Анатолий Корсаков", "Юрий Пеньков", "Илья Сухачев",
            "Иван Маркитан", "Ринат Бибиков", "Вадим Ерошевичев", "Тимур Сейсембаев", "Максим Батырев",
            "Никита Шумский", "Алексей Степанов", "Денис Коротков", "Антон Глушков", "Сергей Индюков",
            "Максим Воронцов", "Евгений Грязнов", "Константин Виролайнен", "Сергей Сердюк", "Павел Дерендяев"],
           ["Евгений Шмаргунов", "Олег Булыгин", "Александр Бардин", "Александр Иванов", "Кирилл Табельский",
            "Александр Ульянцев", "Роман Гордиенко", "Адилет Асканжоев", "Александр Шлейко", "Алена Батицкая",
            "Денис Ежков", "Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Максим Филипенко", "Елена Никитина"],
           ["Евгений Шмаргунов", "Олег Булыгин", "Дмитрий Демидов", "Кирилл Табельский", "Александр Ульянцев",
            "Александр Бардин", "Александр Иванов", "Антон Солонилин", "Максим Филипенко", "Елена Никитина",
            "Азамат Искаков", "Роман Гордиенко"],
           ["Владимир Чебукин", "Эдгар Нуруллин", "Евгений Шек", "Валерий Хаслер", "Татьяна Тен", "Александр Фитискин",
            "Александр Шлейко", "Алена Батицкая", "Александр Беспоясов", "Денис Ежков", "Николай Лопин",
            "Михаил Ларченко"]
           ]

durations1 = [14, 20, 12, 20]
durations2 = [3, 2, 4, 4]
durations3 = [0, 0, 0, 0]
durations4 = [12, 70, 2, 2]


def min_max_course(courses, mentors, durations):
    courses_list = []
    for title, mentor, duration in zip(courses, mentors, durations):
        course_dict = {"title": title, "mentors": mentor, "duration": duration}
        courses_list.append(course_dict)

    min_duration = min(durations)
    max_duration = max(durations)

    maxes = []
    minis = []
    for cou, duration in enumerate(durations):
        if duration == max_duration:
            maxes.append(cou)
        elif duration == min_duration:
            minis.append(cou)

    courses_min = []
    courses_max = []
    for id_course in minis:
        courses_min.append(courses_list[id_course]["title"])
    for id_course in maxes:
        courses_max.append(
            courses_list[id_course]["title"])

    short = f'Самый короткий курс(ы): {", ".join(courses_min)} - {min_duration} месяца(ев)'
    long = f'Самый длинный курс(ы): {", ".join(courses_max)} - {max_duration} месяца(ев)'

    print(short, long, sep='\n')
    return [min_duration, max_duration, courses_min, courses_max]


@pytest.mark.parametrize(
    'durations, expected', (
        [durations1, [["Python-разработчик с нуля"], ["Fullstack-разработчик на Python", "Frontend-разработчик с нуля"]]],
        [durations2, [["Fullstack-разработчик на Python"], ["Python-разработчик с нуля", "Frontend-разработчик с нуля"]]],
        [durations3, [["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"], ["Java-разработчик с нуля", "Fullstack-разработчик на Python", "Python-разработчик с нуля",
           "Frontend-разработчик с нуля"]]],
        [durations4, [["Python-разработчик с нуля",
           "Frontend-разработчик с нуля"], ["Fullstack-разработчик на Python"]]]
    )
)
def test_min_max_duration(durations: list, expected: int):
    result = min_max_course(courses1, mentors1, durations)[2:]
    assert result == expected


@pytest.mark.parametrize(
    'durations, expected', (
        [durations1, [12, 20]],
        [durations2, [2, 4]],
        [durations3, [0, 0]],
        [durations4, [2, 70]]
    )
)
def test_min_max_duration(durations: list, expected: int):
    result = min_max_course(courses1, mentors1, durations)[:2]
    assert result == expected
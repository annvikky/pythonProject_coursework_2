from src.vacancy import Vacancy


def test_vacancy_init(vacancy_1):
    """ Тест на корректность инициализации объекта класса."""
    assert vacancy_1.name == "Должность1"
    assert vacancy_1.url == "https://hh"
    assert vacancy_1.requirement == "Требования1"
    assert vacancy_1.responsibility == "Обязанность1"
    assert vacancy_1.salary == 80000


def test_vacancy_init_without_salary(vacancy_2):
    """ Тест на корректность валидации атрибута 'зарплата'."""
    assert vacancy_2.name == "Должность2"
    assert vacancy_2.url == "https://hh"
    assert vacancy_2.requirement == "Требования2"
    assert vacancy_2.responsibility == "Обязанность2"
    assert vacancy_2.salary == 0


def test_cast_to_object_list(vacancies_list):
    vacancies_objects = Vacancy.cast_to_object_list(vacancies_list)
    vacancy_1 = vacancies_objects[0]
    assert vacancy_1.name == "Python Developer"
    assert vacancy_1.url == "https://hh.ru/vacancy"
    assert vacancy_1.requirement == "Python"
    assert vacancy_1.responsibility == "Can code"
    assert vacancy_1.salary == 1000

    vacancy_2 = vacancies_objects[1]
    assert vacancy_2.name == "Developer"
    assert vacancy_2.url == "https://hh.ru/vacancy"
    assert vacancy_2.requirement == "Thinking"
    assert vacancy_2.responsibility == "Can research"
    assert vacancy_2.salary == 0


def test_cast_to_object_list_and_back(vacancies_list):
    vacancies_objects = Vacancy.cast_to_object_list(vacancies_list)
    vacancies_dict = [vacancy.get_to_dict() for vacancy in vacancies_objects]

    assert vacancies_dict[0]['name'] == vacancies_list[0]['name']
    assert vacancies_dict[0]['url'] == vacancies_list[0]['url']
    assert vacancies_dict[0]['requirement'] == vacancies_list[0]['requirement']
    assert vacancies_dict[0]['responsibility'] == vacancies_list[0]['responsibility']

    assert vacancies_dict[1]['name'] == vacancies_list[1]['name']
    assert vacancies_dict[1]['url'] == vacancies_list[1]['url']
    assert vacancies_dict[1]['requirement'] == vacancies_list[1]['requirement']
    assert vacancies_dict[1]['responsibility'] == vacancies_list[1]['responsibility']


def test_salary_is_bigger(vacancy_1, vacancy_2):
    assert vacancy_1 > vacancy_2


def test_salary_is_smaller(vacancies_list):
    vacancies_objects = Vacancy.cast_to_object_list(vacancies_list)
    assert vacancies_objects[1] < vacancies_objects[0]


def test_salary_is_equal(vacancies_list, vacancy_2):
    vacancies_objects = Vacancy.cast_to_object_list(vacancies_list)
    assert vacancies_objects[1] == vacancy_2

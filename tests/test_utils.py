from src.utils import (get_top_vacancies, get_vacancies_filtered_by_name, get_vacancies_filtered_by_salary_from,
                       sort_vacancies_by_salary)


def test_get_vacancies_filtered_by_name(vacancies_list):
    """Тест на корректность фильтрации по названию вакансии."""
    result = get_vacancies_filtered_by_name(vacancies_list, "Python Developer")
    assert result == [
        {
            "name": "Python Developer",
            "requirement": "Python",
            "responsibility": "Can code",
            "salary": "1000",
            "url": "https://hh.ru/vacancy",
        }
    ]


def test_get_vacancies_filtered_by_salary_from(vacancies_list_2):
    """Тест на корректность фильтрации вакансий по диапазону зарплаты."""
    result = get_vacancies_filtered_by_salary_from(vacancies_list_2, 100000, 120000)
    assert result == [
        {
            "name": "Python Developer",
            "requirement": "Python",
            "responsibility": "Can code",
            "salary": 100000,
            "url": "https://hh.ru/vacancy",
        },
        {
            "name": "C++ Developer",
            "requirement": "C++",
            "responsibility": "Can code",
            "salary": 120000,
            "url": "https://hh.ru/vacancy",
        },
    ]


def test_sort_vacancies_by_salary(vacancies_list_2):
    """Тест на корректность сотртировки вакансий по заплате в порядке убывания."""
    result = sort_vacancies_by_salary(vacancies_list_2)
    assert result == [
        {
            "name": "Java Developer",
            "requirement": "Java",
            "responsibility": "Can code",
            "salary": 150000,
            "url": "https://hh.ru/vacancy",
        },
        {
            "name": "C++ Developer",
            "requirement": "C++",
            "responsibility": "Can code",
            "salary": 120000,
            "url": "https://hh.ru/vacancy",
        },
        {
            "name": "Python Developer",
            "requirement": "Python",
            "responsibility": "Can code",
            "salary": 100000,
            "url": "https://hh.ru/vacancy",
        },
        {
            "name": "Developer",
            "requirement": "Thinking",
            "responsibility": "Can research",
            "salary": 0,
            "url": "https://hh.ru/vacancy",
        },
    ]


def test_get_top_vacancies(vacancies_list_2):
    """Тест на корректность вывода заданного числа топ вакансий по зарплате."""
    result = get_top_vacancies(vacancies_list_2, 3)
    assert result == [
        {
            "name": "Java Developer",
            "requirement": "Java",
            "responsibility": "Can code",
            "salary": 150000,
            "url": "https://hh.ru/vacancy",
        },
        {
            "name": "C++ Developer",
            "requirement": "C++",
            "responsibility": "Can code",
            "salary": 120000,
            "url": "https://hh.ru/vacancy",
        },
        {
            "name": "Python Developer",
            "requirement": "Python",
            "responsibility": "Can code",
            "salary": 100000,
            "url": "https://hh.ru/vacancy",
        },
    ]

import pytest

from src.vacancy import Vacancy


@pytest.fixture
def vacancy_1():
    return Vacancy("Должность1", "https://hh", "Требования1", "Обязанность1",80000)


@pytest.fixture
def vacancy_2():
    return Vacancy("Должность2", "https://hh", "Требования2", "Обязанность2")


@pytest.fixture
def vacancies_list():
    return [
        {'name': 'Python Developer', 'url': 'https://hh.ru/vacancy', 'requirement': 'Python', 'responsibility': 'Can code', 'salary': '1000'},
        {'name': 'Developer', 'url': 'https://hh.ru/vacancy', 'requirement': 'Thinking', 'responsibility': 'Can research'}
    ]
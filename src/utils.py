from src.vacancy import Vacancy


def get_vacancies_filtered_by_name(vacancies: list[Vacancy], search_query: str) -> list[Vacancy]:
    """ Возвращает список вакансий, отфильтрованный по наименовании вакансии."""
    filtered_list = [vacancy for vacancy in vacancies if search_query in vacancy.get('name')]
    return filtered_list


def get_vacancies_filtered_by_salary_from(vacancies: list[Vacancy], salary_from: int) -> list[Vacancy]:
    """ Возвращает список вакансий в заданном диапазоне зарплат от()."""
    vacancies_list = [v for v in vacancies if v.salary >= salary_from]
    return vacancies_list


def sort_vacancies_by_salary(vacancies: list[Vacancy]) -> list[Vacancy]:
    """ Сортирует вакансии по размеру зарплаты в порядке убывания."""
    for v in vacancies:
        if v.get('salary') is None:
            v['salary'] = int(0)
    vacancies_list = sorted(vacancies, key=lambda x: x.get('salary'), reverse=True)
    return vacancies_list


def get_top_vacancies(vacancies: list[Vacancy], top: int) -> list[Vacancy]:
    """ Возвращает заданное число топ вакансий по зарплате."""
    vacancies_list = sort_vacancies_by_salary(vacancies)
    return vacancies_list[:top]

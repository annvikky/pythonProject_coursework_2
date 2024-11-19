from src.hh_api import HH
from src.utils import get_vacancies_filtered_by_name, get_top_vacancies, sort_vacancies_by_salary
from src.vacancies_to_json import SaveToJson
from src.vacancy import Vacancy


def user_interaction():
    """ Функция для взаимодействия с пользователем."""
    search_query = input("Введите запрос для поиска вакансии: ")
    print(f"Мы подбираем вакансии по вашему запросу: {search_query}... Пожалуйста, подождите!\n")

    # получение вакансий по заданному фильтру через подключение к api
    hh_api = HH()
    hh_vacancies = hh_api.get_vacancies(search_query)
    # print(hh_vacancies)

    # сохранение полученных вакансий в json-файл
    saver = SaveToJson()
    saver.add_data(Vacancy.cast_to_object_list(hh_vacancies))

    if hh_vacancies:
        # предложение выбора дальнейших действий с полученными данными
        print("Для максимального соответствия результатов поиска, пожалуйста, выберите действие: ")
        print("1. Показать все вакансии, отобранные по ключевому слову (Введите: 1)")
        print("2. Показать все вакансии, отобранные по названию вакансии (Введите: 2)")
        print("3. Показать количество вакансий, отобранных по зарплате - top (Ведите: 3)")
        print("4. Показать все вакансии в диапазоне зарплат (Введите: 4)")
        print("5. Добавить вакансию (Введите: 5")
        print("6. Удалить вакансию по url\n (Введите: 6")

    try:
        action = int(input("Введите цифру от 1 до 5: "))
    except ValueError:
        print("Ваш выбор не распознан. Выводим данные по действию 1")
        action = 1
    else:
        if action not in range(1, 6):
            print("Ваш выбор не распознан. Выводим данные по действию 1")
            action = 1

    if action == 1:
        for v in Vacancy.cast_to_object_list(hh_vacancies):
            print(v)

    if action == 2:
        filtered_vacations = get_vacancies_filtered_by_name(hh_vacancies, search_query)
        for v in filtered_vacations:
            print(v)

    if action == 3:
        top = int(input("Введите желаемое количество вакансий для вывода: "))
        top_vacancies = get_top_vacancies(hh_vacancies, top)
        for v in top_vacancies:
            print(v)

    if action ==4:





# Функция для взаимодействия с пользователем
# def user_interaction():
#     platforms = ["HeadHunter"]
#     search_query = input("Введите поисковый запрос: ")
#     top_n = int(input("Введите количество вакансий для вывода в топ N: "))
#     filter_words = input("Введите ключевые слова для фильтрации вакансий: ").split()
#     salary_range = input("Введите диапазон зарплат: ") # Пример: 100000 - 150000
#
#     filtered_vacancies = filter_vacancies(vacancies_list, filter_words)
#
#     ranged_vacancies = get_vacancies_by_salary(filtered_vacancies, salary_range)
#
#     sorted_vacancies = sort_vacancies(ranged_vacancies)
#     top_vacancies = get_top_vacancies(sorted_vacancies, top_n)
#     print_vacancies(top_vacancies)


if __name__ == "__main__":
    user_interaction()

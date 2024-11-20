import json
import os
from abc import ABC, abstractmethod
from json import JSONDecodeError
from typing import Any

from src.vacancy import Vacancy


class SaveToFile(ABC):
    """Абстрактный класс для работы с json-файлами."""

    @abstractmethod
    def read_data_from_file(self) -> Any:
        """Абстрактный метод получения данных из файла."""
        pass

    @abstractmethod
    def add_data(self, vacancies: list[Vacancy]) -> Any:
        """Абстрактный метод добавления данных в файл."""
        pass

    @abstractmethod
    def del_data(self, vacancies: list[Vacancy]) -> Any:
        """Абстрактный метод удаления данных из файла."""
        pass


class SaveToJson(SaveToFile):
    def __init__(self, filename="vacancies.json"):
        """Инициализация класса SaveToJson"""
        self.__filename = os.path.join(
            os.path.dirname(os.path.dirname(__file__)),
            "data",
            filename,
        )

    def __read_data_from_file(self) -> list[Vacancy]:
        """Метод для считывания данных из файла"""
        try:
            with open(self.__filename, encoding="utf-8") as file:
                data = json.load(file)
                return Vacancy.cast_to_object_list(data)

        except FileNotFoundError:
            return []
        except JSONDecodeError:
            return []

    def read_data_from_file(self) -> Any:
        return self.__read_data_from_file()

    def __add_data(self, vacancies: list[Vacancy]) -> None:
        """Метод для добавления данных о вакансиях в файл."""
        vacancies_list = self.__read_data_from_file()
        for vacancy in vacancies:
            if vacancy.url in [v.url for v in vacancies_list]:
                return

            with open(self.__filename, encoding="utf-8", mode="a") as file:
                file.write(json.dumps(vacancy.get_to_dict(), indent=4))

    def add_data(self, vacancies) -> Any:
        return self.__add_data(vacancies)

    def __del_data(self, vacancies: list[Vacancy]) -> None:
        """Метод для Удаления данных о вакансии из файла."""
        vacancies_list = self.__read_data_from_file()
        for vacancy in vacancies:

            is_found = False
            for i, v in enumerate(vacancies_list):
                if v.url == vacancy.url:
                    del vacancies_list[i]
                    is_found = True
                    break

            if is_found:
                with open(self.__filename, encoding="utf-8", mode="w") as file:
                    vacancies = [v.get_to_dict() for v in vacancies_list]
                    file.write(json.dumps(vacancies, indent=4))

    def del_data(self, vacancies) -> Any:
        return self.__del_data(vacancies)

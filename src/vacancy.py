class Vacancy:
    """Класс для работы с вакансиями."""

    __slots__ = ("name", "url", "salary", "requirement", "responsibility")

    def __init__(
        self,
        name: str,
        url: str,
        requirement: str,
        responsibility: str,
        salary: int = 0,
    ):
        self.name = name
        self.url = url
        self.requirement = requirement
        self.responsibility = responsibility
        self.salary = self.__salary_is_valid(salary)

    @staticmethod
    def __salary_is_valid(salary: int):
        """Метод для валидации зарплаты."""
        if salary:
            return int(salary)
        else:
            return 0

    @classmethod
    def cast_to_object_list(cls, vacancies: list[dict]) -> list["Vacancy"]:
        """Возвращает список экземпляров класса из списка словарей."""
        return [cls(**vacancy) for vacancy in vacancies]

    def get_to_dict(self):
        """Возвращает словарь с описанием вакансии из экземпляра класса."""
        return {
            "name": self.name,
            "url": self.url,
            "requirement": self.requirement,
            "responsibility": self.responsibility,
            "salary": self.salary,
        }

    def __eq__(self, other):
        """Магический метод сравнения вакансий по зарплате (=)."""
        if not isinstance(other, (int, Vacancy)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")

        salary_for_comparison = other if isinstance(other, int) else other.salary
        return self.salary == salary_for_comparison

    def __lt__(self, other):
        """Магический метод сравнения вакансий по зарплате (<)."""
        if not isinstance(other, (int, Vacancy)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")

        salary_for_comparison = other if isinstance(other, int) else other.salary
        return self.salary < salary_for_comparison

    def __gt__(self, other):
        """Магический метод сравнения вакансий по зарплате (>)."""
        if not isinstance(other, (int, Vacancy)):
            raise TypeError("Операнд справа должен иметь тип int или Vacancy")

        salary_for_comparison = other if isinstance(other, int) else other.salary
        return self.salary > salary_for_comparison

    def __str__(self):
        """Метод строкового представления вакансий."""

        return f"""{self.name} (Зарплата: {self.salary if self.salary else 'не указана'}).
Требования: {self.requirement}.
Обязанности: {self.responsibility}.
Ссылка на вакансию: {self.url}."""

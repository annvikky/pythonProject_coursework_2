from unittest.mock import MagicMock, patch

from src.hh_api import HH


@patch("requests.get")
def test_get_vacancies(mock_get):
    """ Тест на корректность получения вакансий через mock запроса."""
    response_body = {
        "items": [
            {
                "name": "Python Developer",
                "salary": {"from": "1000"},
                "alternate_url": "https://hh.ru/vacancy",
                "snippet": {"requirement": "Python", "responsibility": "Can code"},
            },
            {
                "name": "Developer",
                "alternate_url": "https://hh.ru/vacancy",
                "snippet": {
                    "requirement": "Thinking",
                    "responsibility": "Can research",
                },
            },
        ]
    }

    mock_response = MagicMock()
    mock_response.status_code = 200
    mock_response.json.return_value = response_body

    mock_get.return_value = mock_response

    hh = HH()
    # Вызываем метод get_vacancies
    keyword = "Developer"
    vacancies = hh.get_vacancies(keyword)

    # Проверяем, что requests.get возвращает правильный результат
    assert len(vacancies) == 2
    assert vacancies[0]["name"] == response_body["items"][0]["name"]
    assert vacancies[1]["name"] == response_body["items"][1]["name"]

    # Проверяем, что requests.get вызывался с правильными аргументами
    mock_get.assert_called_with(
        "https://api.hh.ru/vacancies",
        headers={"User-Agent": "HH-User-Agent"},
        params={"text": keyword, "page": 0, "per_page": 100},
    )

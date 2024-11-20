import os
from unittest.mock import mock_open, patch

from src.vacancies_to_json import SaveToJson

data = "{'name': 'Python Developer', 'url': 'https://', 'requirement': 'P', 'responsibility': 'Can', 'salary': 100000}"


def test_read_data_from_file():
    """Тест на открытие файла."""
    m = mock_open(read_data=data)
    saver = SaveToJson("test")

    with patch("builtins.open", m):
        result = saver.read_data_from_file()
    path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "data", "test")
    m.assert_called_once_with(path, encoding="utf-8")
    assert result == []

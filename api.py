import json

import requests


class Person:
    """API библиотека к веб приложению _______________________"""

    def __init__(self):
        self.base_url = 'https://______________/'

    def get_api_key_name_email(self, name: str, email: str) -> json:
        """Метод делает запрос к API сервера и возвращает статус запроса и результат в формате
        JSON с уникальным ключём пользователя, найденного под указанным name и email"""

        headers = {
            'name': name,
            'email': email,
        }
        res = requests.get(self.base_url + 'api/key', headers=headers)
        status = res.status_code
        result = ""
        try:
            result = res.json()
        except json.decoder.JSONDecodeError:
            result = res.text
        return status, result
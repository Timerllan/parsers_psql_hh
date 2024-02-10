from HH_get.abstract import AbstractGetter
from parsers_psql_hh.vacancies import Vacancies
import requests


class HH(AbstractGetter):

    def __init__(self):
        self.api = 'https://api.hh.ru/vacancies/?text='

    def get_request(self, user_input):
        response = requests.get(f'{self.api}{user_input}&per_page=100')
        result = []
        if response.status_code == 200:
            data = response.json()
            for x in data['items']:
                salary = x.get('salary')
                if salary and salary['from'] != 0 and salary['to'] != 0 and salary['from'] is not None and salary[
                    'to'] is not None:
                    vacancy = Vacancies(x['id'], x['name'], x['employer']['name'], x['salary']['from'],
                                        x['salary']['to'],
                                        x['area']['name'], x['area']['url'])
                    result.append(vacancy)

        else:
            print("Ошибка запроса:", response.status_code)

        return result




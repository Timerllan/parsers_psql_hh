from abstract_hh import HHAbstract
import requests


class HH(HHAbstract):

    def __init__(self):
        self.api = 'https://api.hh.ru/vacancies/?text='

    def _get_request(self, user_input):
        response = requests.get(f'{self.api}{user_input}&per_page=100')

        if response.status_code == 200:
            result = []
            data = response.json()
            for x in data['items']:
                salary = x.get('salary')
                if salary and salary['from'] != 0 and salary['to'] != 0 and salary['from'] is not None and salary[
                    'to'] is not None:
                    result.append(x)
            return result

        else:
            print("Ошибка запроса:", response.status_code)



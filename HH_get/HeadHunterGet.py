from abstract_hh import HHAbstract
import requests


class HH(HHAbstract):

    def __init__(self):
        self.api = 'https://api.hh.ru/vacancies/?text='

    def get_request(self, user_input):
        response = requests.get(f'{self.api}{user_input}')
        if response.status_code == 200:
            return response.json()
        else:
            raise ConnectionError('Ошибка соединения:'.format(response.status_code))

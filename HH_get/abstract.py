from abc import ABC, abstractmethod


class AbstractGetter(ABC):
    '''Функция делает звпрос на получение данных с HH '''

    @abstractmethod
    def get_request(self, user_input):
        pass



from abc import ABC, abstractmethod

from vacancies import Vacancies


class DBManagerAbstract(ABC):

    @abstractmethod
    def add_vacancy(self, vacancy: Vacancies):
        pass

    @abstractmethod
    def get_companies_and_vacancies_count(self):
        '''получает список всех компаний и количество вакансий у каждой компании.'''
        pass

    @abstractmethod
    def get_all_vacancies(self) -> list[Vacancies]:
        '''получает список всех вакансий с указанием названия компании,
        названия вакансии и зарплаты и ссылки на вакансию.'''
        pass

    @abstractmethod
    def get_avg_salary(self):
        '''получает среднюю зарплату по вакансиям.'''
        pass

    @abstractmethod
    def get_vacancies_with_higher_salary(self):
        """получает список всех вакансий, у которых зарплата выше средней по всем вакансиям."""
        pass

    @abstractmethod
    def get_vacancies_with_keyword(self, user_input) -> list[Vacancies]:
        """получает список всех вакансий,
        в названии которых содержатся переданные в метод слова, например python."""
        pass

class Vacancies:

    def __init__(self, id_vacancy, name_vacancy, name_company, salary_from, salary_to, city, url):
        self.url = url
        self.city = city
        self.salary_to = salary_to
        self.salary_from = salary_from
        self.name_company = name_company
        self.name_vacancy = name_vacancy
        self.id_vacancy = id_vacancy

    def __str__(self):
        return (f'id Вакансии :{self.id_vacancy},\n'
                f'Имя Вакансии :{self.name_vacancy},\n'
                f'Имя Компании :{self.name_company},\n'
                f'Зарплата от :{self.salary_from},\n'
                f'Зарплата до :{self.salary_to},\n'
                f'Город :{self.city},\n'
                f'URL :{self.url}\n')

    def __repr__(self):
        return str(self)

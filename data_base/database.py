from abc import ABC

import psycopg2
from HH_get.HeadHunterGet import HH
from vacancies import Vacancies
from data_base.Abstract_Psql import DBManagerAbstract


class DBManager(DBManagerAbstract):

    def get_vacancies_with_keyword(self, user_input) -> list[Vacancies]:
        result = []
        cursor = self.connect()
        cursor.execute(
            "select id_vacancy, name_vacancy, name_company, salary_from, salary_to, city, url from vacancies "
            "WHERE lower(name_vacancy) LIKE %s", (f'%{user_input.lower()}%',))
        for id_vacancy, name_vacancy, name_company, salary_from, salary_to, city, url in cursor.fetchall():
            result.append(Vacancies(id_vacancy, name_vacancy, name_company, salary_from, salary_to, city, url))
        cursor.close()
        for vacancy in result:
            print(vacancy)

    def get_vacancies_with_higher_salary(self):
        result = []
        cursor = self.connect()
        cursor.execute(
            """select * from vacancies where
            (salary_from + salary_to / 2) > (SELECT AVG(salary_from + salary_to / 2)
            FROM vacancies);""")
        for id_vacancy, name_vacancy, name_company, salary_from, salary_to, city, url in cursor.fetchall():
            result.append(Vacancies(id_vacancy, name_vacancy, name_company, salary_from, salary_to, city, url))
        cursor.close()
        for vacancy in result:
            print(vacancy)

    def get_avg_salary(self):
        cursor = self.connect()
        cursor.execute("""(SELECT round(AVG(salary_from + salary_to / 2),2)
        FROM
        vacancies);""")
        b = cursor.fetchone()[0]
        cursor.close()
        return f"средняя зарплата {b}"

    def get_all_vacancies(self):
        result = []
        cusror = self.connect()
        cusror.execute('select * from vacancies')
        for id_vacancy, name_vacancy, name_company, salary_from, salary_to, city, url in cusror.fetchall():
            result.append(Vacancies(id_vacancy, name_vacancy, name_company, salary_from, salary_to, city, url))
        return result

    def get_companies_and_vacancies_count(self):
        cursor = self.connect()
        cursor.execute("""select count(name_company),name_company from vacancies
            group by name_company""")
        b = cursor.fetchall()
        cursor.close()
        for i in b:
            print(f"кол-во вакансий {i[0]}, назвние компаний {i[1]}")

    def __init__(self, dbname='vacancies_hh', host='localhost', user='postgres', password=None):
        self.user = user
        self.host = host
        self.dbname = dbname
        self.password = password
        cursor = self.connect()
        self.prepare(cursor)
        cursor.close()

    def connect(self):
        conn = psycopg2.connect(host=self.host,
                                database=self.dbname,
                                user=self.user,
                                password=self.password
                                )
        conn.autocommit = True
        cursor = conn.cursor()

        return cursor

    def prepare(self, cursor):
        # cursor.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (self.dbname,))
        # if not cursor.fetchone():
        #     #cursor.execute(f"CREATE DATABASE {self.dbname}")
        #     print(f"База данных {self.dbname} создана.")
        # else:
        #     print(f"База данных {self.dbname} уже была создана")

        # cursor.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = vacancies)")
        # table_exists = cursor.fetchone()[0]

        # if not table_exists:

        # cursor.execute(
        #     'CREATE TABLE vacancies (id_vacancy int,'
        #     'name_vacancy varchar(250),'
        #     'name_company varchar(250) not null, '
        #     'salary_from int not null,'
        #     'salary_to int not null,'
        #     'city varchar(100) not null),'
        #     'url varchar(100) not null')
        # print(f"Таблица vacancies создана.")

        # if cursor.rowcount > 0:
        #     print("Данные добавлены в таблицу.")
        # else:
        #     print("Данные дублируются и не были добавлены.")
        pass

    def add_vacancy(self, vacancies: Vacancies):
        cursor = self.connect()
        cursor.execute("INSERT INTO vacancies (id_vacancy, "
                       "name_vacancy, "
                       "name_company, "
                       "salary_from, salary_to, city,URL) "
                       "VALUES (%s,%s,%s,%s,%s,%s,%s)"
                       " ON CONFLICT (id_vacancy) DO NOTHING", (vacancies.id_vacancy,
                                                                vacancies.name_vacancy,
                                                                vacancies.name_company,
                                                                vacancies.salary_from,
                                                                vacancies.salary_to,
                                                                vacancies.city,
                                                                vacancies.url))

        if cursor.rowcount > 0:
            print("Данные добавлены в таблицу.")
        else:
            print("Данные дублируются и не были добавлены.")
        cursor.close()

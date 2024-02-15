import psycopg2
from data_base.database import DBManager
from HH_get.HeadHunterGet import HH
from parsers_psql_hh.Create_T_DB import CreateDB
import os


def main():
    password = "password_psql"

    ctdb = CreateDB(password=f"{password}")
    hh = HH()

    bdname = "vacancies_hh"

    conn = psycopg2.connect(host='localhost'
                            , user='postgres'
                            , password=f"{password}")
    conn.autocommit = True

    cur = conn.cursor()
    cur.execute("SELECT 1 FROM pg_catalog.pg_database WHERE datname = %s", (bdname,))
    if not cur.fetchone():
        ctdb.create_db()
    else:
        print("база данных существует")

    conn = psycopg2.connect(database=f"{bdname}"
                            , host='localhost'
                            , user='postgres'
                            , password=f"{password}")
    conn.autocommit = True

    cur = conn.cursor()

    cur.execute("SELECT EXISTS(SELECT 1 FROM information_schema.tables WHERE table_name = 'vacancies')")
    table_exists = cur.fetchone()[0]
    if not table_exists:
        ctdb.create_table()
    else:
        print("Таблица существет")

    cur.execute("ALTER TABLE vacancies DROP CONSTRAINT IF EXISTS id_vacancy_unique")
    cur.execute("ALTER TABLE vacancies ADD CONSTRAINT id_vacancy_unique UNIQUE (id_vacancy)")

    cur.close()
    conn.close()

    req = hh.get_request('python')

    db = DBManager(password=f"{password}")
    for result in req:
        db.add_vacancy(result)
    print("получает список всех вакансий,"
          "в названии которых содержатся переданные в метод слова, например python.\n")
    db.get_vacancies_with_keyword('junior')
    print('--------------------------------------------------------------------------')

    print("получает список всех вакансий, у которых зарплата выше средней по всем вакансиям.\n")
    db.get_vacancies_with_higher_salary()
    print('--------------------------------------------------------------------------')

    print('получает среднюю зарплату по вакансиям.\n')
    print(f'{db.get_avg_salary()}')
    print('--------------------------------------------------------------------------')

    print('получает список всех компаний и количество вакансий у каждой компании.\n')
    db.get_companies_and_vacancies_count()
    print('--------------------------------------------------------------------------')

    print(
        'получает список всех вакансий с указанием названия компании,названия вакансии'
        ' и зарплаты и ссылки на вакансию.')
    print(db.get_all_vacancies())


if __name__ == '__main__':
    main()

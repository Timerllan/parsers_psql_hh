from data_base.database import DBManager


def main():
    password_sql = input("введите пароль бд")
    db = DBManager(password=f"{password_sql}")

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

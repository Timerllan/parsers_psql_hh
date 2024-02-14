import psycopg2


class CreateDB:

    def __init__(self, dbname="vacancies_hh", host='localhost', user='postgres', password="Shepetok2000"):
        self.dbname = dbname
        self.password = password
        self.user = user
        self.host = host

    def create_db(self):
        conn = psycopg2.connect(
            user=self.user,
            password=self.password,
            host=self.host
        )

        conn.autocommit = True
        # Create a new database
        cur = conn.cursor()
        cur.execute("CREATE DATABASE vacancies_hh")

        # Close the cursor and connection
        cur.close()
        conn.close()

    def create_table(self):
        conn = psycopg2.connect(
            database=self.dbname,
            user=self.user,
            password=self.password,
            host=self.host
        )

        conn.autocommit = True
        # Create a new database
        cur = conn.cursor()
        cur.execute(
            'CREATE TABLE vacancies (id_vacancy int primary key,'
            'name_vacancy varchar(250),'
            'name_company varchar(250) not null,'
            'salary_from int not null,'
            'salary_to int not null,'
            'city varchar(100) not null,'
            'url varchar(100) not null)'
        )
        # Close the cursor and connection
        cur.close()
        conn.close()




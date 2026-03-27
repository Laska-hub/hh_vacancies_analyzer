from hh_vacancies_analyzer.db import get_connection


def create_tables() -> None:
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS companies (
                    id SERIAL PRIMARY KEY,
                    company_id INT UNIQUE,
                    name TEXT
                );
                """
            )

            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS vacancies (
                    id SERIAL PRIMARY KEY,
                    vacancy_id INT UNIQUE,
                    name TEXT,
                    salary_from INT,
                    salary_to INT,
                    company_id INT REFERENCES companies(company_id)
                );
                """
            )

    conn.close()
    print("Таблицы созданы!")


if __name__ == "__main__":
    create_tables()

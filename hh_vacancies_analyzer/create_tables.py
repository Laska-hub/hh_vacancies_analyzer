# hh_vacancies_analyzer/create_tables.py
"""Создание таблиц companies и vacancies в базе hh_vacancies."""

from hh_vacancies_analyzer.db import get_connection


def create_tables() -> None:
    """Создает таблицы в базе данных, если они не существуют."""
    conn = get_connection()
    with conn:
        with conn.cursor() as cursor:
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS companies (
                    id SERIAL PRIMARY KEY,
                    company_id INT UNIQUE,
                    name TEXT,
                    area TEXT,
                    url TEXT
                );
                """
            )
            cursor.execute(
                """
                CREATE TABLE IF NOT EXISTS vacancies (
                    id SERIAL PRIMARY KEY,
                    vacancy_id INT UNIQUE,
                    title TEXT,
                    salary_from INT,
                    salary_to INT,
                    url TEXT,
                    company_id INT REFERENCES companies(company_id)
                );
                """
            )
    conn.close()


if __name__ == "__main__":
    create_tables()

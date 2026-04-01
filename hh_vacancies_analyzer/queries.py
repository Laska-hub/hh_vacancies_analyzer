# hh_vacancies_analyzer/queries.py
"""SQL-запросы для анализа вакансий."""

from typing import List, Tuple

from hh_vacancies_analyzer.db import get_cursor


def get_companies_and_vacancies_count() -> List[Tuple[str, int]]:
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT c.name, COUNT(v.id)
            FROM companies c
            LEFT JOIN vacancies v ON c.company_id = v.company_id
            GROUP BY c.name
            ORDER BY COUNT(v.id) DESC;
            """
        )
        return cursor.fetchall()


def get_all_vacancies() -> List[Tuple[str, str, int, int, str]]:
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT c.name, v.title, v.salary_from, v.salary_to, v.url
            FROM vacancies v
            JOIN companies c ON v.company_id = c.company_id;
            """
        )
        return cursor.fetchall()


def get_avg_salary() -> float:
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT AVG((salary_from + salary_to) / 2)
            FROM vacancies;
            """
        )
        result = cursor.fetchone()
        return float(result[0]) if result and result[0] else 0.0


def get_vacancies_with_higher_salary() -> List[Tuple[str, str, int, int]]:
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT c.name, v.title, v.salary_from, v.salary_to
            FROM vacancies v
            JOIN companies c ON v.company_id = c.company_id
            WHERE (salary_from + salary_to) / 2 > (
                SELECT AVG((salary_from + salary_to) / 2) FROM vacancies
            );
            """
        )
        return cursor.fetchall()


def get_vacancies_with_keyword(keyword: str) -> List[Tuple[str, str]]:
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT c.name, v.title
            FROM vacancies v
            JOIN companies c ON v.company_id = c.company_id
            WHERE LOWER(v.title) LIKE LOWER(%s);
            """,
            (f"%{keyword}%",),
        )
        return cursor.fetchall()

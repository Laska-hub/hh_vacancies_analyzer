# hh_vacancies_analyzer/ui.py
"""UI для работы с базой hh_vacancies."""

import logging
from typing import List, Optional, Tuple

from hh_vacancies_analyzer.db import get_cursor

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def get_companies_and_vacancies_count() -> (
    List[Tuple[str, str, Optional[int], Optional[int], str]]
):
    """Возвращает список всех компаний с количеством вакансий и ссылкой на сайт."""
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT c.name, c.area, v.salary_from, v.salary_to, c.url
            FROM companies c
            JOIN vacancies v ON c.company_id = v.company_id;
            """
        )
        result: List[Tuple[str, str, Optional[int], Optional[int], str]] = (
            cursor.fetchall()
        )
    return result


def get_all_vacancies_with_salary() -> List[Tuple[str, str, int, int]]:
    """Возвращает все вакансии с указанием компании и диапазона зарплат."""
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT v.title, c.name, v.salary_from, v.salary_to
            FROM vacancies v
            JOIN companies c ON v.company_id = c.company_id;
            """
        )
        result: List[Tuple[str, str, int, int]] = cursor.fetchall()
    return result


def get_avg_salary() -> Optional[float]:
    """Возвращает среднюю зарплату по всем вакансиям (среднее (salary_from + salary_to)/2)."""
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT AVG((salary_from + salary_to)/2.0)
            FROM vacancies
            WHERE salary_from IS NOT NULL AND salary_to IS NOT NULL;
            """
        )
        row = cursor.fetchone()
        if row and row[0] is not None:
            return float(row[0])
    return None


def get_vacancies_above_avg() -> List[Tuple[str, str, int, int]]:
    """Возвращает вакансии с зарплатой выше средней."""
    avg_salary = get_avg_salary()
    if avg_salary is None:
        return []
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT v.title, c.name, v.salary_from, v.salary_to
            FROM vacancies v
            JOIN companies c ON v.company_id = c.company_id
            WHERE ((v.salary_from + v.salary_to)/2.0) > %s;
            """,
            (avg_salary,),
        )
        result: List[Tuple[str, str, int, int]] = cursor.fetchall()
    return result


def get_vacancies_with_keyword(keyword: str) -> List[Tuple[str, str]]:
    """Возвращает вакансии, где в названии встречается ключевое слово."""
    with get_cursor() as cursor:
        cursor.execute(
            """
            SELECT title, url
            FROM vacancies
            WHERE title ILIKE %s;
            """,
            (f"%{keyword}%",),
        )
        result: List[Tuple[str, str]] = cursor.fetchall()
    return result


def main() -> None:
    """Главная функция UI."""
    logger.info("Запуск UI приложения hh_vacancies_analyzer")

    # Пример использования всех функций
    companies_vacancies = get_companies_and_vacancies_count()
    logger.info("Компании с вакансиями: %d записей", len(companies_vacancies))

    all_vacancies = get_all_vacancies_with_salary()
    logger.info("Все вакансии с зарплатой: %d записей", len(all_vacancies))

    avg_salary = get_avg_salary()
    logger.info("Средняя зарплата: %s", avg_salary)

    high_salary_vacancies = get_vacancies_above_avg()
    logger.info(
        "Вакансии выше средней зарплаты: %d записей", len(high_salary_vacancies)
    )

    keyword = "Python"
    python_vacancies = get_vacancies_with_keyword(keyword)
    logger.info(
        "Вакансии с ключевым словом '%s': %d записей", keyword, len(python_vacancies)
    )

    logger.info("Работа UI приложения завершена")


if __name__ == "__main__":
    main()

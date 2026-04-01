# hh_vacancies_analyzer/manager.py
"""Функции для вставки компаний и вакансий в базу данных."""

import logging
from typing import Any, Dict

from hh_vacancies_analyzer.db import get_cursor

logger = logging.getLogger(__name__)


def insert_company(company: Dict[str, Any]) -> int:
    """
    Вставляет компанию в базу данных.
    Возвращает ID компании (company_id).
    """
    with get_cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO companies (company_id, name, area, url)
            VALUES (%s, %s, %s, %s)
            ON CONFLICT (company_id) DO UPDATE SET
                name = EXCLUDED.name,
                area = EXCLUDED.area,
                url = EXCLUDED.url
            RETURNING company_id;
            """,
            (
                int(company["id"]),
                company.get("name"),
                (company.get("area") or {}).get("name"),
                company.get("url"),
            ),
        )
        result = cursor.fetchone()
        company_id: int = result[0]  # возвращаем company_id
        logger.info(
            "Вставлена/обновлена компания: %s (%s)", company.get("name"), company_id
        )
        return company_id


def insert_vacancy(vacancy: Dict[str, Any], company_id: int) -> None:
    """
    Вставляет вакансию в базу данных с указанием company_id.
    """
    with get_cursor() as cursor:
        cursor.execute(
            """
            INSERT INTO vacancies (vacancy_id, title, salary_from, salary_to, url, company_id)
            VALUES (%s, %s, %s, %s, %s, %s)
            ON CONFLICT (vacancy_id) DO UPDATE SET
                title = EXCLUDED.title,
                salary_from = EXCLUDED.salary_from,
                salary_to = EXCLUDED.salary_to,
                url = EXCLUDED.url,
                company_id = EXCLUDED.company_id;
            """,
            (
                int(vacancy["id"]),
                vacancy.get("name") or vacancy.get("title"),
                vacancy.get("salary_from"),
                vacancy.get("salary_to"),
                vacancy.get("alternate_url") or vacancy.get("url"),
                company_id,
            ),
        )
        logger.info(
            "Вставлена/обновлена вакансия: %s (компания %s)",
            vacancy.get("name") or vacancy.get("title"),
            company_id,
        )


def populate_companies_and_vacancies() -> None:
    """
    Разрывает цикл импорта для UI.
    Вызывает main из populate_db.
    """
    from hh_vacancies_analyzer.populate_db import main

    main()

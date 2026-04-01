# hh_vacancies_analyzer/populate_db.py
"""Заполнение базы данных."""

import logging
from typing import Any, Dict, List

from hh_vacancies_analyzer.api import get_companies, get_vacancies
from hh_vacancies_analyzer.manager import insert_company, insert_vacancy

logger = logging.getLogger(__name__)


def _extract_salary(vacancy: Dict[str, Any]) -> tuple[int | None, int | None]:
    salary = vacancy.get("salary") or {}
    return salary.get("from"), salary.get("to")


def main() -> None:
    logger.info("Запуск заполнения базы")

    companies: List[Dict[str, Any]] = get_companies()

    for company in companies:
        company_id = insert_company(company)

        vacancies = get_vacancies(company_id)

        for vacancy in vacancies:
            salary_from, salary_to = _extract_salary(vacancy)

            vacancy_data: Dict[str, Any] = {
                "id": vacancy["id"],
                "name": vacancy.get("name"),
                "salary_from": salary_from,
                "salary_to": salary_to,
                "alternate_url": vacancy.get("alternate_url"),
            }

            insert_vacancy(vacancy_data, company_id)

    logger.info("База успешно заполнена")

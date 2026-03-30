# hh_vacancies_analyzer/populate_db.py
"""Заполняет базу компаний и вакансий, используя HH API и manager."""

import logging
from typing import Any, Dict, List

from hh_vacancies_analyzer.api import fetch_companies, fetch_vacancies
from hh_vacancies_analyzer.manager import insert_company, insert_vacancy

logger = logging.getLogger(__name__)
logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(levelname)s - %(message)s"
)


def main() -> None:
    """Заполняет базу компаний и вакансий."""
    logger.info("Запуск populate_db.py")
    companies: List[Dict[str, Any]] = fetch_companies()
    for company in companies:
        company_id: int = insert_company(company)
        vacancies: List[Dict[str, Any]] = fetch_vacancies(company_id)
        for vacancy in vacancies:
            insert_vacancy(vacancy, company_id)
    logger.info("Заполнение базы завершено успешно!")


if __name__ == "__main__":
    main()

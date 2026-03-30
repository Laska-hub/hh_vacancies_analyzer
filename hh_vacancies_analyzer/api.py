# hh_vacancies_analyzer/api.py
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import logging
import requests

from hh_vacancies_analyzer.config import HH_BASE_URL

logger = logging.getLogger(__name__)


def _fetch_items(endpoint: str, params: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
    """
    Универсальный метод для получения элементов с HH API.
    endpoint: путь после базового URL, например "employers" или "vacancies"
    params: словарь с параметрами запроса
    """
    url = urljoin(HH_BASE_URL, endpoint)
    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        items = data.get("items", [])
        logger.info("Получено %d элементов с %s", len(items), endpoint)
        return items
    except requests.RequestException as e:
        logger.error("Ошибка при запросе %s: %s", url, e)
        return []


def fetch_companies(page: int = 0, per_page: int = 100) -> List[Dict[str, Any]]:
    """
    Получает список компаний (employers) с HH API.
    """
    params = {"page": page, "per_page": per_page}
    return _fetch_items("employers", params=params)


def fetch_vacancies(company_id: int, page: int = 0, per_page: int = 100) -> List[Dict[str, Any]]:
    """
    Получает список вакансий конкретной компании с HH API.
    """
    params = {"employer_id": company_id, "page": page, "per_page": per_page}
    return _fetch_items("vacancies", params=params)

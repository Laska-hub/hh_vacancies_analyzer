# hh_vacancies_analyzer/api.py
"""Работа с HH API."""

import logging
import time
from typing import Any, Dict, List, Optional
from urllib.parse import urljoin

import requests

from hh_vacancies_analyzer.config import HH_BASE_URL

logger = logging.getLogger(__name__)

EMPLOYER_IDS: List[int] = [
    3529,  # Сбер
    78638,  # Т-Банк
    15478,  # VK
    80,  # Лукойл
    2180,  # Ozon
]


def _request(endpoint: str, params: Optional[Dict[str, Any]] = None) -> Dict[str, Any]:
    url = urljoin(HH_BASE_URL, endpoint)

    for attempt in range(3):
        try:
            response = requests.get(url, params=params, timeout=10)
            response.raise_for_status()
            return response.json()
        except requests.RequestException as error:
            logger.warning("Ошибка запроса (%s), попытка %s", error, attempt + 1)
            time.sleep(1)

    logger.error("Не удалось получить данные с HH API")
    return {}


def get_companies() -> List[Dict[str, Any]]:
    companies: List[Dict[str, Any]] = []

    for employer_id in EMPLOYER_IDS:
        data = _request(f"employers/{employer_id}")
        if data:
            companies.append(data)

    return companies


def get_vacancies(company_id: int) -> List[Dict[str, Any]]:
    data = _request(
        "vacancies",
        params={"employer_id": company_id, "per_page": 100},
    )
    return data.get("items", [])

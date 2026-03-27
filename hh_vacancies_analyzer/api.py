from typing import Any, Dict, List, cast

import requests

BASE_URL = "https://api.hh.ru/employers"


def fetch_companies(page: int = 0) -> List[Dict[str, Any]]:
    params = {"page": page, "per_page": 100}
    response = requests.get(BASE_URL, params=params, timeout=10)
    response.raise_for_status()
    data = cast(Dict[str, Any], response.json())
    return cast(List[Dict[str, Any]], data.get("items", []))


def fetch_vacancies(company_id: int) -> List[Dict[str, Any]]:
    url = "https://api.hh.ru/vacancies"
    params = {"employer_id": company_id, "per_page": 100}
    response = requests.get(url, params=params, timeout=10)
    response.raise_for_status()
    data = cast(Dict[str, Any], response.json())
    return cast(List[Dict[str, Any]], data.get("items", []))


def get_companies_data(pages: int = 1) -> List[Dict[str, Any]]:
    companies: List[Dict[str, Any]] = []
    for page in range(pages):
        companies.extend(fetch_companies(page))
    return companies


def get_vacancies_data(company_id: int) -> List[Dict[str, Any]]:
    return fetch_vacancies(company_id)

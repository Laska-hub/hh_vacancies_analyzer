from typing import Any, Dict, List

from hh_vacancies_analyzer.manager import insert_company, insert_vacancy


# Пример функций получения данных с HH
def get_companies_data() -> List[Dict[str, Any]]:
    # Получаем список компаний с API
    return [
        {"name": "Company A", "description": "Desc A"},
        {"name": "Company B", "description": "Desc B"},
    ]


def get_vacancies_data(company_id: int) -> List[Dict[str, Any]]:
    # Получаем список вакансий по company_id
    return [
        {"title": "Dev", "salary_from": 1000, "salary_to": 2000, "url": "http://..."}
    ]


def main() -> None:
    """Заполняет базу компаний и вакансий"""
    companies = get_companies_data()
    for company in companies:
        company_id = insert_company(company)
        if company_id is not None:  # проверяем, что ID получен
            vacancies = get_vacancies_data(company_id)
            for vacancy in vacancies:
                insert_vacancy(vacancy, company_id)
    print("Заполнение базы завершено успешно!")


if __name__ == "__main__":
    print("Запуск populate_db.py")
    main()  # или как у тебя называется функция заполнения базы
    print("Заполнение базы завершено!")

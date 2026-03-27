from typing import Any, Dict, Optional


# Пример функций вставки в базу
def insert_company(company: Dict[str, Any]) -> Optional[int]:
    """
    Вставляет компанию в базу и возвращает её ID.
    Если вставка не удалась — возвращает None.
    """
    # Тут логика вставки в БД
    # Например:
    # result = db_insert(...)
    # return result.id
    return 1  # заглушка для примера


def insert_vacancy(vacancy: Dict[str, Any], company_id: int) -> None:
    """
    Вставляет вакансию в базу с указанием ID компании.
    """
    # Логика вставки вакансии
    pass


# Функция для UI, разрывает цикл импорта
def populate_companies_and_vacancies() -> None:
    """
    Заполняет базу компаний и вакансий, вызывая main из populate_db.
    """
    from hh_vacancies_analyzer.populate_db import main

    main()

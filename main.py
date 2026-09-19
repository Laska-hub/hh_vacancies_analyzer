# main.py
"""Единая точка входа в приложение."""

import logging

from hh_vacancies_analyzer.create_tables import create_tables
from hh_vacancies_analyzer.db import create_database
from hh_vacancies_analyzer.populate_db import main as populate_db
from hh_vacancies_analyzer.ui import main as ui_main


def main() -> None:
    logging.basicConfig(level=logging.INFO)

    print("Создание базы данных...")
    create_database()

    print("Создание таблиц...")
    create_tables()

    print("Загрузка данных...")
    populate_db()

    print("Запуск интерфейса...")
    ui_main()


if __name__ == "__main__":
    main()

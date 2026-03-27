from contextlib import contextmanager
from typing import Generator

import psycopg2
from psycopg2.extensions import connection
from psycopg2.extensions import cursor as psycopg2_cursor

from hh_vacancies_analyzer.config import DB_HOST, DB_NAME, DB_PASSWORD, DB_PORT, DB_USER


def get_connection() -> connection:
    return psycopg2.connect(
        host=DB_HOST,
        database=DB_NAME,
        user=DB_USER,
        password=DB_PASSWORD,
        port=DB_PORT,
    )


@contextmanager
def get_cursor() -> Generator[psycopg2_cursor, None, None]:
    """
    Контекстный менеджер для работы с курсором базы данных.
    """
    conn = get_connection()
    try:
        with conn:
            with conn.cursor() as cursor:
                yield cursor
    finally:
        conn.close()


def create_database() -> None:
    """
    Создание базы данных, если она не существует
    """
    try:
        conn = psycopg2.connect(
            host=DB_HOST,
            database=DB_NAME,
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
        )
        conn.close()
        print(f"База данных '{DB_NAME}' уже существует, пропускаем создание.")
    except psycopg2.OperationalError:
        # Соединение не удалось — создаём базу данных через соединение с postgres
        conn = psycopg2.connect(
            host=DB_HOST,
            database="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
        )
        conn.autocommit = True
        with conn.cursor() as cur:
            cur.execute(f'CREATE DATABASE "{DB_NAME}"')
        conn.close()
        print(f"База данных '{DB_NAME}' успешно создана.")

import logging
from contextlib import contextmanager
from typing import Generator

import psycopg2
from psycopg2.extensions import connection
from psycopg2.extensions import cursor as psycopg2_cursor

from hh_vacancies_analyzer.config import (DB_HOST, DB_NAME, DB_PASSWORD,
                                          DB_PORT, DB_USER)

logger = logging.getLogger(__name__)


def get_connection() -> connection:
    """
    Создает и возвращает подключение к базе данных.
    """
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
    Автоматически управляет транзакцией и закрытием соединения.
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
    Создает базу данных, если она не существует.
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
        logger.info("База данных '%s' уже существует", DB_NAME)

    except psycopg2.OperationalError:
        conn = psycopg2.connect(
            host=DB_HOST,
            database="postgres",
            user=DB_USER,
            password=DB_PASSWORD,
            port=DB_PORT,
        )
        conn.autocommit = True

        try:
            with conn.cursor() as cur:
                cur.execute(f'CREATE DATABASE "{DB_NAME}"')
            logger.info("База данных '%s' успешно создана", DB_NAME)
        finally:
            conn.close()

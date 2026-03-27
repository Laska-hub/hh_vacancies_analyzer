# config.py
import os

from dotenv import load_dotenv

# Загружаем .env файл
load_dotenv()

DB_NAME = os.getenv("DB_NAME", "hh_db")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")
DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = os.getenv("DB_PORT", "5432")

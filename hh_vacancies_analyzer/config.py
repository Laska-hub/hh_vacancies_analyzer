# hh_vacancies_analyzer/config.py

import os

from dotenv import load_dotenv

load_dotenv()

HH_BASE_URL = "https://api.hh.ru/"

DB_HOST = os.getenv("DB_HOST", "localhost")
DB_PORT = int(os.getenv("DB_PORT", 5432))
DB_NAME = os.getenv("DB_NAME", "hh_vacancies")
DB_USER = os.getenv("DB_USER", "postgres")
DB_PASSWORD = os.getenv("DB_PASSWORD", "postgres")

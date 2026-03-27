# HH Vacancies Analyzer

Проект для получения и анализа вакансий и компаний с [HeadHunter](https://hh.ru) 
с последующей загрузкой в базу данных.

## Структура проекта

hh_vacancies_analyzer/
├── hh_vacancies_analyzer/
│ ├── init.py
│ ├── api.py # функции для запросов к HH API
│ ├── manager.py # функции для работы с БД (insert, wrapper)
│ ├── populate_db.py # main для заполнения БД
│ ├── ui.py # точка входа для запуска

├── pyproject.toml # настройки Poetry
├── README.md
└── .gitignore
----create_db.py
----poetry.lock
----.env
----.flake8


## Установка

1. Клонируем репозиторий:

```bash
git clone <your_repo_url>
cd hh_vacancies_analyzer
Создаем виртуальное окружение и устанавливаем зависимости:poetry install
Активируем виртуальное окружение (если нужно вручную):poetry shell
Запуск
1. Через пакет (рекомендуется)

Запуск наполнения базы данными через модуль:

poetry run python -m hh_vacancies_analyzer.populate_db

Запуск интерфейса/основного скрипта:

poetry run python -m hh_vacancies_analyzer.ui
2. Прямой запуск скрипта

❌ Не рекомендуется после того, как скрипт перенесен внутрь пакета — прямой запуск python populate_db.py не сработает.

- Проверка кода
Mypy (статическая типизация):
poetry run mypy .
Flake8 (PEP8, стиль кода):
poetry run flake8 .
Black (форматирование кода):
poetry run black .
Isort (сортировка импортов):
poetry run isort .

 -Возможные ошибки и решения
ModuleNotFoundError / ImportError:
Убедитесь, что используете запуск через -m внутри пакета, а не прямой путь к файлу.
403 Client Error при запросе к HH API:
Некоторые компании не разрешают просмотр вакансий через API. Скрипт обрабатывает это и выводит сообщение в лог.
can't adapt type 'dict':
Ошибка при вставке в БД, если структура словаря не соответствует ожидаемой схеме. 
Проверьте функции insert_company и insert_vacancy.
Структура функций
hh_vacancies_analyzer.api.get_companies_data(pages: int) → список компаний
hh_vacancies_analyzer.api.get_vacancies_data(company_id: int) → список вакансий
hh_vacancies_analyzer.manager.insert_company(company: dict) → вставка компании в БД
hh_vacancies_analyzer.manager.insert_vacancy(vacancy: dict, company_id: int) → вставка вакансии в БД
hh_vacancies_analyzer.populate_db.main() → функция для заполнения базы
hh_vacancies_analyzer.ui → интерфейс для запуска скрипта

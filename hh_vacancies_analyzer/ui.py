import logging

from hh_vacancies_analyzer.manager import populate_companies_and_vacancies

logger = logging.getLogger(__name__)


def main() -> None:
    """Главная функция интерфейса пользователя."""
    logging.basicConfig(level=logging.INFO)
    logger.info("Запуск UI приложения hh_vacancies_analyzer")

    # Вызываем функцию, которая заполняет базу компаний и вакансий
    populate_companies_and_vacancies()

    logger.info("Работа UI приложения завершена")


if __name__ == "__main__":
    main()

from hh_vacancies_analyzer.manager import populate_companies_and_vacancies


def main_ui() -> None:
    print("Запуск UI...")
    populate_companies_and_vacancies()


if __name__ == "__main__":
    main_ui()

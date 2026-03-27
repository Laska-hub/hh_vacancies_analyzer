from typing import Optional


class Company:
    def __init__(self, company_id: int, name: str) -> None:
        self.company_id = company_id
        self.name = name


class Vacancy:
    def __init__(
        self,
        vacancy_id: int,
        name: str,
        salary_from: Optional[int],
        salary_to: Optional[int],
        company_id: int,
    ) -> None:
        self.vacancy_id = vacancy_id
        self.name = name
        self.salary_from = salary_from
        self.salary_to = salary_to
        self.company_id = company_id

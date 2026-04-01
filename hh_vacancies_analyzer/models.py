from dataclasses import dataclass
from typing import Optional


@dataclass(slots=True)
class Company:
    id: int
    name: str
    area: Optional[str]
    url: str


@dataclass(slots=True)
class Vacancy:
    id: int
    name: str
    salary_from: Optional[int]
    salary_to: Optional[int]
    url: str
    employer_id: int

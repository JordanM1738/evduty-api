from dataclasses import dataclass
from typing import List

from evdutyapi.car import Car


@dataclass(frozen=True)
class Account:
    balance: str
    email: int
    cars: List[Car]
    currentCarId: str

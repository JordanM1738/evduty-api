from dataclasses import dataclass
from typing import Any, Dict, List
from evdutyapi.account import Account
from evdutyapi.api_response.car_response import CarResponse
from evdutyapi.car import Car


@dataclass(frozen=True)
class AccountResponse:
    balance: str
    email: str
    cars: List[Car]
    currentCarId: str

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> Account:
        return Account(balance=data['balance'],
                        email=data['email'],
                       currentCarId=data['currentCarId'],
                       cars=[CarResponse.from_json(c) for c in data['cars']])

from dataclasses import dataclass
from typing import Any, Dict
from evdutyapi.car import Car


@dataclass(frozen=True)
class CarResponse:
    id: str
    name: str
    year: int
    color: str
    imageUrl: str

    @classmethod
    def from_json(cls, data: Dict[str, Any]) -> Car:
        return Car(id=data['id'],
                        name=data['name'],
                        year=data['year'],
                        color=data['color'],
                       imageUrl=data['imageUrl'])

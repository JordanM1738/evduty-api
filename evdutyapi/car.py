from dataclasses import dataclass


@dataclass(frozen=True)
class Car:
    id: str
    name: str
    year: int
    color: str
    imageUrl: str

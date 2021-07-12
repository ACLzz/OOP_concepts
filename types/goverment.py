from dataclasses import dataclass
from types.human import Human


@dataclass
class TaxPayer:
    human: Human
    balance: int = 0
    tax: float = 0.2

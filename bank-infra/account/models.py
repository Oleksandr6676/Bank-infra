from dataclasses import dataclass, field

@dataclass
class Account:
    id: int
    account_number: str
    owner: str
    balance: float = field(default=0.0)
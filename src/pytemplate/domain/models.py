from dataclasses import dataclass


@dataclass
class Burger:
    bread: str
    patty: str
    sauce: str | None = None
    toppings: list[str] | None = None

    def __str__(self):
        return f"{self.bread} {self.patty} {self.sauce or 'no sauce'} {self.toppings or 'no toppings'} "

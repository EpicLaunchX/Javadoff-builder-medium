from dataclasses import dataclass


@dataclass
class Burger:
    bread: str
    patty: str
    sauce: list[str] = None
    toppings: list[str] = None

    def __str__(self):
        return f"{self.bread} {self.patty} {self.sauce or 'no sauce'} {self.toppings or 'no toppings'} "

# -*- coding: utf-8 -*-
class Good:
    model_name = "Personal Computer"

    def __init__(self, our_model, cpu, speed, prod_year):
        """Przeciążenie metody"""
        print("Cześć - jestem init!")
        self.model = our_model
        self.cpu_name = cpu
        self.speed = speed
        self.prod_year = prod_year
        self.__serial = None
        print(f"Utworzyliśmy obiekt ID {id(self)}")

    def opis(self):
        print(f"Jestem {self.model_name} - modelem {self.model} z procesorem {self.cpu_name}")

    def set_model(self, new_model):
        print(f"Changing model from {self.model} to {new_model}")
        self.model = new_model

    def history(self):
        print(f"Computer {self.model} was born in {self.prod_year}")
        print(F"Was {3400/self.speed} time slower than today 3400 MHz")


computer_X = Good
computer_0 = Good("Komputer AT", '8086', 4, 1932)
computer_1 = Good("Komputer XT", '286', 12, 2343)
computer_2 = Good("Komputer XV", 'Pentium/586', 133, 2322)

for comp in (computer_0, computer_1, computer_2):
    comp.history()
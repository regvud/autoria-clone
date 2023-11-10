from django.db import models


class CurrencyChoices(models.TextChoices):
    USD = "USD"
    UAH = "UAH"
    EUR = "EUR"


class BodyChoices(models.TextChoices):
    Jeep = "Jeep"
    Sedan = "Sedan"
    Hatchback = "Hatchback"
    SUV = "SUV"
    Coupe = "Coupe"
    Van = "Van"
    Minivan = "Minivan"
    Convertible = "Convertible"
    Roadster = "Roadster"
    Muscle_Car = "Muscle car"

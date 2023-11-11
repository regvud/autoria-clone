from django.db import models


class RoleChoices(models.TextChoices):
    Admin = "Admin"
    Manager = "Manager"
    Sale = "Sale"
    Mechanic = "Mechanic"

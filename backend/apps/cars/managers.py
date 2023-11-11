from django.db.models import Manager


class CarManager(Manager):
    def avg_price(self, price):
        return self.filter(price__gt=price)

from django.db import models
from django.contrib.auth.models import User

PRODUCT_CHOICES = (
    ("TV", 'tv'),
    ("IPAD", 'ipad'),
    ("PLAYSTATION", 'playstation'),
)


class Sale(models.Model):
    product = models.CharField(max_length=20, choices=PRODUCT_CHOICES)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    total = models.FloatField(blank=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self) -> str:
        return f"{self.product} - {self.quantity}"

    def save(self, *args, **kwargs):
        price = None
        if self.product == 'TV':
            price = 600.80
        elif self.product == 'IPAD':
            price = 200.99
        elif self.product == 'PLAYSTATION':
            price = 300.80
        else:
            pass
        self.total = price * self.quantity
        super().save(*args, **kwargs)

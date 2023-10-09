from django.db import models
from django.contrib.auth.models import User

CURRENCY_CHOICES = [
    ('KZT', 'Казахстанский тенге(KZT)'),
    ('RUB', 'Российский рубль(RUB)'),
    ('UZS', 'Узбекистанский сум(UZS)'),

]

class Profile(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True)
    currency = models.CharField(max_length=3, choices=CURRENCY_CHOICES)
    email = models.EmailField(blank=False)
    #created_at = models.DateTimeField(auto_now_add=True,null=True)

    def __str__(self):
        return f'{self.user}'






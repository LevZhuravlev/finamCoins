from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Equities(models.Model):
    company_name = models.CharField(max_length=128)
    price = models.IntegerField()
    company_label = models.ImageField(null=True, blank=True, upload_to="images/", verbose_name="company_logo")

    def __str__(self):
        return self.company_name

class FinCoins(models.Model):
    user_name = models.OneToOneField(User, on_delete=models.CASCADE)
    coins = models.IntegerField(default=0, blank=True, null=True)

    def __str__(self):
        return str(self.coins)
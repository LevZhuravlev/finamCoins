from django.contrib import admin
from .models import Equities, FinCoins

# Register your models here.

admin.site.register(Equities)
admin.site.register(FinCoins)
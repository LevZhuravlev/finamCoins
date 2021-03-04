from django.urls import path
from .views import open

urlpatterns = [
    path('', open)
]

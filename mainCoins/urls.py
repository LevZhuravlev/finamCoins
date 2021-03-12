from django.urls import path
from .views import open, MyProjectLoginView, RegisterUserView, MyProjectLogout, equitiess

urlpatterns = [
    path('', open),
    path('login', MyProjectLoginView.as_view(), name='login'),
    path('registration', RegisterUserView.as_view(), name='registration'),
    path('logout', MyProjectLogout.as_view(), name='logout'),
    path('allequitiess', equitiess, name='allequitiess'),

]

from django.contrib import admin
from .models import Equities, Groups, StudentsInfo, TeachersInfo

# Register your models here.

admin.site.register(Equities)

admin.site.register(Groups)
admin.site.register(StudentsInfo)
admin.site.register(TeachersInfo)
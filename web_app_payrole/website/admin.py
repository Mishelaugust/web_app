from django.contrib import admin
from .models import Client,Profile, Salary

admin.site.register(Client)
admin.site.register(Profile)
admin.site.register(Salary)
from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import post_save
from django.dispatch import receiver

class Client(models.Model):
    client_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    phone_number = models.CharField(max_length=11)
    email = models.CharField(max_length=100)
    address = models.CharField(max_length=200)
    dietary_needs = models.CharField(max_length=200)
    medical_conditions = models.CharField(max_length=200)
    date_added = models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return(f"{self.first_name} {self.last_name}")
    
class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    job_titles = (
        ('mg','Менеджер'),
        ('dd','водитель доставщик')
    )
    branches = (
        ('s','Отдел продаж'),
        ('d','Отдел доставки')
    )
    job_title = models.CharField(max_length=2, choices=job_titles,default='')
    branch = models.CharField(max_length=1,choices=branches,default='')
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')
    salary = models.DecimalField(max_digits=10, decimal_places=2)


class Salary(models.Model):
    job_titles = (
        ('mg','Менеджер'),
        ('dd','водитель доставщик')
    )
    salary_user = models.DecimalField(max_digits=10, decimal_places=2)
    name_job_title = models.CharField(max_length=2, choices=job_titles,default='')
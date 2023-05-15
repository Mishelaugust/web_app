# Generated by Django 4.1.7 on 2023-05-14 23:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('website', '0002_profile'),
    ]

    operations = [
        migrations.CreateModel(
            name='Salary',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('salary_user', models.DecimalField(decimal_places=2, max_digits=10)),
                ('name_job_title', models.CharField(choices=[('mg', 'Менеджер'), ('dd', 'водитель доставщик')], default='', max_length=2)),
            ],
        ),
    ]
# Generated by Django 3.1.7 on 2021-05-10 15:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainCoins', '0022_auto_20210506_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsinfo',
            name='father_name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='studentsinfo',
            name='phone_number',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Отчество'),
        ),
        migrations.AddField(
            model_name='studentsinfo',
            name='second_name',
            field=models.CharField(blank=True, max_length=32, null=True, verbose_name='Фамилия'),
        ),
    ]

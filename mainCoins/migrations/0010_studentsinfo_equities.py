# Generated by Django 3.1.7 on 2021-04-29 08:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainCoins', '0009_studentsinfo'),
    ]

    operations = [
        migrations.AddField(
            model_name='studentsinfo',
            name='equities',
            field=models.ManyToManyField(to='mainCoins.Equities'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-04-29 07:40

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('mainCoins', '0004_status'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Status',
        ),
    ]
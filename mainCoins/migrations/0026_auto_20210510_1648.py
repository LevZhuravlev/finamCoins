# Generated by Django 3.1.7 on 2021-05-10 16:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainCoins', '0025_studentsinfo_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsinfo',
            name='slug',
            field=models.SlugField(blank=True, default=None, max_length=150, null=True, unique=True),
        ),
    ]
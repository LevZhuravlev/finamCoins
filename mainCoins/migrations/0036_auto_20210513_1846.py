# Generated by Django 3.1.7 on 2021-05-13 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainCoins', '0035_auto_20210513_1843'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersinfo',
            name='is_super_user',
            field=models.BooleanField(default=False, verbose_name='Суперадмин'),
        ),
    ]

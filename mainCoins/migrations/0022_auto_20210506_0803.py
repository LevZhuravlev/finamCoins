# Generated by Django 3.1.7 on 2021-05-06 08:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainCoins', '0021_auto_20210506_0602'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersinfo',
            name='group',
            field=models.ManyToManyField(blank=True, to='mainCoins.Groups'),
        ),
    ]

# Generated by Django 3.1.7 on 2021-05-06 06:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainCoins', '0019_auto_20210506_0553'),
    ]

    operations = [
        migrations.AlterField(
            model_name='teachersinfo',
            name='group',
            field=models.ManyToManyField(blank=True, null=True, to='mainCoins.Groups'),
        ),
    ]

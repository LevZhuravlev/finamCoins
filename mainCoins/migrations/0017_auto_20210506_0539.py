# Generated by Django 3.1.7 on 2021-05-06 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainCoins', '0016_delete_fincoins'),
    ]

    operations = [
        migrations.AlterField(
            model_name='studentsinfo',
            name='equities',
            field=models.ManyToManyField(blank=True, to='mainCoins.Equities'),
        ),
        migrations.AlterField(
            model_name='studentsinfo',
            name='group',
            field=models.ManyToManyField(blank=True, to='mainCoins.Groups'),
        ),
    ]

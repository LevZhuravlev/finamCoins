# Generated by Django 3.1.7 on 2021-05-17 07:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainCoins', '0043_auto_20210517_0708'),
    ]

    operations = [
        migrations.AddField(
            model_name='equities',
            name='company_label_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]

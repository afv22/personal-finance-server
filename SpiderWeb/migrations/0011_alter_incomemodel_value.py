# Generated by Django 4.1.1 on 2022-09-25 16:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("SpiderWeb", "0010_rename_payoutvalue_incomemodel_value"),
    ]

    operations = [
        migrations.AlterField(
            model_name="incomemodel",
            name="value",
            field=models.FloatField(default=0),
        ),
    ]

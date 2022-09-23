# Generated by Django 4.1.1 on 2022-09-23 15:54

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("SpiderWeb", "0005_alter_usermodel_state_incomemodel"),
    ]

    operations = [
        migrations.CreateModel(
            name="AccountModel",
            fields=[
                (
                    "id",
                    models.PositiveBigIntegerField(primary_key=True, serialize=False),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                    ),
                ),
            ],
        ),
    ]

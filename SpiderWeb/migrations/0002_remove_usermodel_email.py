# Generated by Django 4.1 on 2022-09-12 20:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ("SpiderWeb", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="usermodel",
            name="email",
        ),
    ]

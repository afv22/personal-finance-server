# Generated by Django 4.1.1 on 2022-09-23 19:45

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("SpiderWeb", "0007_delete_nodemodel"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="accountmodel",
            name="id",
        ),
        migrations.RemoveField(
            model_name="accountmodel",
            name="name",
        ),
        migrations.RemoveField(
            model_name="accountmodel",
            name="user",
        ),
        migrations.RemoveField(
            model_name="incomemodel",
            name="id",
        ),
        migrations.RemoveField(
            model_name="incomemodel",
            name="name",
        ),
        migrations.RemoveField(
            model_name="incomemodel",
            name="user",
        ),
        migrations.CreateModel(
            name="NodeModel",
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
        migrations.AddField(
            model_name="accountmodel",
            name="nodemodel_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=693600,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="SpiderWeb.nodemodel",
            ),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name="incomemodel",
            name="nodemodel_ptr",
            field=models.OneToOneField(
                auto_created=True,
                default=693600,
                on_delete=django.db.models.deletion.CASCADE,
                parent_link=True,
                primary_key=True,
                serialize=False,
                to="SpiderWeb.nodemodel",
            ),
            preserve_default=False,
        ),
    ]

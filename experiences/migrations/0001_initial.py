# Generated by Django 4.1.1 on 2022-09-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Experience",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("country", models.CharField(default="한국", max_length=50)),
                ("city", models.CharField(default="서울", max_length=80)),
                ("name", models.CharField(max_length=250)),
                ("price", models.PositiveIntegerField()),
                ("address", models.CharField(max_length=250)),
                ("start_at", models.TimeField()),
                ("end_at", models.TimeField()),
                ("description", models.TextField()),
            ],
            options={"abstract": False,},
        ),
        migrations.CreateModel(
            name="Perk",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("created_at", models.DateTimeField(auto_now_add=True)),
                ("updated_at", models.DateTimeField(auto_now=True)),
                ("name", models.CharField(max_length=100)),
                ("detail", models.TextField(blank=True, max_length=150, null=True)),
                (
                    "explanation",
                    models.TextField(blank=True, max_length=150, null=True),
                ),
            ],
            options={"abstract": False,},
        ),
    ]

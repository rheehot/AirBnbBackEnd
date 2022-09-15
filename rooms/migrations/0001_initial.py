# Generated by Django 4.1.1 on 2022-09-15 14:15

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Amenity",
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
                ("name", models.CharField(max_length=150)),
                (
                    "description",
                    models.TextField(blank=True, max_length=150, null=True),
                ),
            ],
            options={"verbose_name_plural": "Amenities",},
        ),
        migrations.CreateModel(
            name="Room",
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
                ("name", models.CharField(default="", max_length=200)),
                ("country", models.CharField(default="한국", max_length=50)),
                ("city", models.CharField(default="서울", max_length=80)),
                ("price", models.PositiveIntegerField()),
                ("rooms", models.PositiveIntegerField()),
                ("toilets", models.PositiveIntegerField()),
                ("description", models.TextField()),
                ("address", models.CharField(max_length=250)),
                ("pet_friendly", models.BooleanField(default=True)),
                (
                    "kind",
                    models.CharField(
                        choices=[
                            ("entire", "Entire Place"),
                            ("private", "Private Room"),
                            ("shared", "Shared Room"),
                        ],
                        max_length=20,
                    ),
                ),
                (
                    "amenities",
                    models.ManyToManyField(related_name="rooms", to="rooms.amenity"),
                ),
            ],
            options={"abstract": False,},
        ),
    ]

# Generated by Django 4.2 on 2024-02-03 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="EmployeeInfo",
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
                ("first_name", models.CharField(max_length=50)),
                ("last_name", models.CharField(max_length=50)),
                ("position", models.CharField(max_length=50)),
                ("salary", models.DecimalField(decimal_places=2, max_digits=10)),
                ("date_of_birth", models.DateField()),
                ("address", models.CharField(max_length=255)),
                ("phone", models.CharField(max_length=15)),
                ("email", models.EmailField(max_length=254)),
                ("hire_date", models.DateField()),
                ("status", models.CharField(max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name="RoomType",
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
                ("name", models.CharField(max_length=255)),
                ("description", models.TextField()),
                (
                    "price_per_night",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("capacity", models.IntegerField()),
                (
                    "room_type",
                    models.CharField(
                        choices=[
                            ("Deluxe Room", "Deluxe Room"),
                            ("Standard Room", "Standard Room"),
                            ("Normal Room", "Normal Room"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
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
                ("room_number", models.IntegerField()),
                (
                    "room_type",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        related_name="rooms",
                        to="management.roomtype",
                    ),
                ),
            ],
            options={
                "ordering": ("room_number",),
            },
        ),
    ]
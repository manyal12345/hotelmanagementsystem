# Generated by Django 4.2 on 2024-02-03 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ("accounting", "0001_initial"),
        ("reception", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="payment",
            name="booking",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="reception.booking"
            ),
        ),
        migrations.AddField(
            model_name="bill",
            name="guest",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="reception.guest"
            ),
        ),
    ]

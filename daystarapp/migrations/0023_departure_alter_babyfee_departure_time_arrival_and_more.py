# Generated by Django 5.0.4 on 2024-05-01 06:06

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daystarapp", "0022_alter_babyfee_amount_paid_and_more"),
    ]

    operations = [
        migrations.CreateModel(
            name="Departure",
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
                (
                    "departure_time",
                    models.DateTimeField(verbose_name="Time of Departure"),
                ),
                (
                    "taker_name",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Baby picked by:",
                    ),
                ),
                (
                    "comment",
                    models.CharField(
                        blank=True, max_length=100, null=True, verbose_name="Comment"
                    ),
                ),
            ],
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="departure_time",
            field=models.DateTimeField(null=True, verbose_name="Time of Departure"),
            preserve_default=False,
        ),
        migrations.CreateModel(
            name="Arrival",
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
                ("arrival_time", models.DateTimeField(verbose_name="Time of Arrival")),
                (
                    "bringer_name",
                    models.CharField(
                        blank=True,
                        max_length=50,
                        null=True,
                        verbose_name="Baby brought in by:",
                    ),
                ),
                (
                    "period_of_stay",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("Morning", "Morning"),
                            ("Afternoon", "Afternoon"),
                            ("Evening", "Evening"),
                            ("Whole Day", "Whole Day"),
                        ],
                        max_length=50,
                        null=True,
                    ),
                ),
                (
                    "l_name",
                    models.ForeignKey(
                        blank=True,
                        on_delete=django.db.models.deletion.CASCADE,
                        to="daystarapp.sitter",
                        verbose_name="Assigned to Sitter",
                    ),
                ),
            ],
        ),
        migrations.DeleteModel(
            name="At_school",
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-01 10:16

import daystarapp.models
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "daystarapp",
            "0024_at_school_remove_arrival_l_name_delete_departure_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="baby",
            name="baby_number",
            field=models.CharField(
                blank=True,
                default=0,
                max_length=4,
                null=True,
                validators=[
                    daystarapp.models.validate_two_digit_integer,
                    django.core.validators.RegexValidator(
                        message="Value must be a two-digit integer", regex="^\\d{1,2}$"
                    ),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="departure_time",
            field=models.DateTimeField(null=True, verbose_name="Time of Departure"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="s_number",
            field=models.CharField(
                blank=True,
                max_length=4,
                null=True,
                validators=[
                    daystarapp.models.validate_two_digit_integer,
                    django.core.validators.RegexValidator(
                        message="Value must be a two-digit integer", regex="^\\d{1,2}$"
                    ),
                ],
                verbose_name="Sitter Number",
            ),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-01 11:50

import daystarapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daystarapp", "0028_alter_babyfee_departure_time_alter_sitter_s_contact"),
    ]

    operations = [
        migrations.AlterField(
            model_name="babyfee",
            name="departure_time",
            field=models.DateTimeField(null=True, verbose_name="Time of Departure"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="rec_contact",
            field=models.CharField(
                blank=True,
                default=1,
                max_length=10,
                validators=[daystarapp.models.validate_phone_number],
                verbose_name="Recommender's Contact",
            ),
            preserve_default=False,
        ),
    ]

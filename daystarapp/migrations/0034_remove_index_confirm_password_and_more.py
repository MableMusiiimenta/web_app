# Generated by Django 5.0.4 on 2024-05-02 09:28

import daystarapp.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daystarapp", "0033_alter_babyfee_departure_time"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="index",
            name="confirm_password",
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="departure_time",
            field=models.DateTimeField(null=True, verbose_name="Time of Departure"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="index",
            name="password",
            field=models.CharField(max_length=50, verbose_name="Admin Password"),
        ),
        migrations.AlterField(
            model_name="index",
            name="username",
            field=models.CharField(
                max_length=50,
                validators=[daystarapp.models.validate_two_names],
                verbose_name="Administrator's Name",
            ),
        ),
    ]

# Generated by Django 5.0.4 on 2024-05-01 12:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daystarapp", "0030_alter_at_school_bringer_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="babyfee",
            name="departure_time",
            field=models.DateTimeField(null=True, verbose_name="Time of Departure"),
            preserve_default=False,
        ),
    ]

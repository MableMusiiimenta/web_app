# Generated by Django 5.0.4 on 2024-04-27 20:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "daystarapp",
            "0014_alter_babyfee_departure_time_alter_dollsale_l_name_and_more",
        ),
    ]

    operations = [
        migrations.AlterField(
            model_name="babyfee",
            name="departure_time",
            field=models.DateTimeField(null=True, verbose_name="Time of Departure"),
            preserve_default=False,
        ),
    ]

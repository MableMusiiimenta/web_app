# Generated by Django 5.0.4 on 2024-05-01 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daystarapp", "0026_alter_baby_parent_contact_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="babyfee",
            name="departure_time",
            field=models.DateTimeField(null=True, verbose_name="Time of Departure"),
            preserve_default=False,
        ),
    ]

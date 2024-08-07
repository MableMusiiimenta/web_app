# Generated by Django 5.0.4 on 2024-04-26 06:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        (
            "daystarapp",
            "0011_alter_babyfee_payment_date_alter_dollsale_sale_date_and_more",
        ),
    ]

    operations = [
        migrations.AddField(
            model_name="dollsale",
            name="price",
            field=models.DecimalField(
                blank=True,
                decimal_places=2,
                max_digits=10,
                null=True,
                verbose_name="Price",
            ),
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="departure_time",
            field=models.DateTimeField(null=True, verbose_name="Time of Departure"),
            preserve_default=False,
        ),
    ]

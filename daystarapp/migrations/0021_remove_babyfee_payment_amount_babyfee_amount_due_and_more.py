# Generated by Django 5.0.4 on 2024-04-30 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daystarapp", "0020_alter_babyfee_departure_time_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="babyfee",
            name="payment_amount",
        ),
        migrations.AddField(
            model_name="babyfee",
            name="amount_due",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="Amount Due"
            ),
        ),
        migrations.AddField(
            model_name="babyfee",
            name="amount_paid",
            field=models.DecimalField(
                decimal_places=2, default=0, max_digits=10, verbose_name="Amount Paid"
            ),
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="departure_time",
            field=models.DateTimeField(null=True, verbose_name="Time of Departure"),
            preserve_default=False,
        ),
    ]
# Generated by Django 5.0.4 on 2024-05-18 12:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daystarapp", "0075_alter_babyfee_departure_time_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="babyfee",
            name="departure_time",
            field=models.DateTimeField(null=True, verbose_name="Time of Departure"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="payment_date",
            field=models.DateField(null=True, verbose_name="Payment Date"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="doll",
            name="stock_date",
            field=models.DateField(null=True, verbose_name="Stock Date"),
        ),
        migrations.AlterField(
            model_name="dollsale",
            name="sale_date",
            field=models.DateField(null=True, verbose_name="Sale Date"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="dob",
            field=models.DateField(null=True, verbose_name="Date of Birth"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitterpayment",
            name="attendance_date",
            field=models.DateField(null=True, verbose_name="Date"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="supply",
            name="date_of_today",
            field=models.DateField(null=True, verbose_name="Date"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="supply",
            name="expiry_date",
            field=models.DateField(null=True, verbose_name="Expiry Date"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="supply",
            name="qty_stocked",
            field=models.IntegerField(default=0, verbose_name="Quantity Stocked"),
        ),
    ]

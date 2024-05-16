# Generated by Django 5.0.4 on 2024-05-15 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daystarapp", "0068_alter_babyfee_departure_time_and_more"),
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
            name="buying_price",
            field=models.IntegerField(default=None, verbose_name="Buying Price"),
        ),
        migrations.AlterField(
            model_name="doll",
            name="price",
            field=models.DecimalField(
                decimal_places=2,
                default=None,
                max_digits=10,
                verbose_name="Selling Price",
            ),
        ),
        migrations.AlterField(
            model_name="doll",
            name="qty_in_stock",
            field=models.IntegerField(default=None, verbose_name="Quantity in Stock"),
        ),
        migrations.AlterField(
            model_name="doll",
            name="qty_left",
            field=models.IntegerField(default=None, verbose_name="Quantity Left"),
        ),
        migrations.AlterField(
            model_name="doll",
            name="qty_stocked",
            field=models.IntegerField(default=None, verbose_name="Quantity Stocked"),
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
            name="date_stocked",
            field=models.DateField(null=True, verbose_name="Date Stocked"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="supply",
            name="expiry_date",
            field=models.DateField(null=True, verbose_name="Expiry Date"),
            preserve_default=False,
        ),
    ]

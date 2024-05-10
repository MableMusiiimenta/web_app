# Generated by Django 5.0.4 on 2024-05-07 09:24

import daystarapp.models
import django.core.validators
import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daystarapp", "0039_alter_baby_gender_alter_babyfee_departure_time"),
    ]

    operations = [
        migrations.AlterField(
            model_name="at_school",
            name="bringer_name",
            field=models.CharField(
                default=1,
                max_length=50,
                validators=[daystarapp.models.validate_two_names],
                verbose_name="Baby brought in by:",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="at_school",
            name="comment",
            field=models.CharField(default=1, max_length=100, verbose_name="Comment"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="at_school",
            name="l_name",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.CASCADE,
                to="daystarapp.sitter",
                verbose_name="Assigned to Sitter",
            ),
        ),
        migrations.AlterField(
            model_name="at_school",
            name="period_of_stay",
            field=models.CharField(
                choices=[
                    ("Morning", "Morning"),
                    ("Afternoon", "Afternoon"),
                    ("Evening", "Evening"),
                    ("Whole Day", "Whole Day"),
                ],
                default=1,
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="at_school",
            name="taker_name",
            field=models.CharField(
                default=1,
                max_length=50,
                validators=[daystarapp.models.validate_two_names],
                verbose_name="Baby picked by:",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="baby",
            name="baby_number",
            field=models.CharField(
                default=0,
                max_length=4,
                validators=[
                    daystarapp.models.validate_two_digit_integer,
                    django.core.validators.RegexValidator(
                        message="Value must be a two-digit integer", regex="^\\d{1,2}$"
                    ),
                ],
            ),
        ),
        migrations.AlterField(
            model_name="baby",
            name="first_name",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="baby",
            name="gender",
            field=models.CharField(
                choices=[("Female", "Female"), ("Male", "Male")],
                default=1,
                max_length=10,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="baby",
            name="last_name",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="baby",
            name="location",
            field=models.CharField(default=1, max_length=50),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="baby",
            name="parent_contact",
            field=models.CharField(
                default=1,
                max_length=50,
                validators=[daystarapp.models.validate_phone_number],
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="baby",
            name="parent_name",
            field=models.CharField(
                default=1,
                max_length=50,
                validators=[daystarapp.models.validate_two_names],
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="amount_paid",
            field=models.CharField(
                max_length=7,
                validators=[django.core.validators.RegexValidator("^[0-9]+$")],
                verbose_name="Price",
            ),
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="departure_time",
            field=models.DateTimeField(null=True, verbose_name="Time of Departure"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="l_name",
            field=models.ForeignKey(
                max_length=100,
                on_delete=django.db.models.deletion.CASCADE,
                to="daystarapp.baby",
                verbose_name="For Baby",
            ),
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="pay_for",
            field=models.CharField(
                choices=[("Half-day", "Half-day"), ("Full-day", "Full-day")],
                default=1,
                max_length=20,
                verbose_name="Pay For",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="payment_date",
            field=models.DateField(null=True, verbose_name="Payment Date"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="payment_method",
            field=models.CharField(
                choices=[
                    ("Cash", "Cash"),
                    ("Cheque", "Cheque"),
                    ("Mobile Money", "Mobile Money"),
                    ("Bank Transfer", "Bank Transfer"),
                ],
                default=1,
                max_length=50,
                verbose_name="Mode of Payment",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="categorystay",
            name="name",
            field=models.CharField(
                choices=[
                    ("Morning", "Morning"),
                    ("Afternoon", "Afternoon"),
                    ("Evening", "Evening"),
                    ("Whole Day", "Whole Day"),
                ],
                default=1,
                max_length=50,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="doll",
            name="brand",
            field=models.CharField(default=1, max_length=100, verbose_name="Brand"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="doll",
            name="color",
            field=models.CharField(default=1, max_length=50, verbose_name="Color"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="doll",
            name="price",
            field=models.DecimalField(
                decimal_places=2, default=1, max_digits=10, verbose_name="Cost"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="dollsale",
            name="l_name",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE,
                to="daystarapp.baby",
                verbose_name="Sold To",
            ),
        ),
        migrations.AlterField(
            model_name="dollsale",
            name="price",
            field=models.CharField(
                max_length=7,
                validators=[django.core.validators.RegexValidator("^[0-9]+$")],
                verbose_name="Price",
            ),
        ),
        migrations.AlterField(
            model_name="dollsale",
            name="quantity_sold",
            field=models.PositiveIntegerField(default=1, verbose_name="Quantity Sold"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="dollsale",
            name="sale_date",
            field=models.DateField(null=True, verbose_name="Sale Date"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="dollsale",
            name="total_amount",
            field=models.DecimalField(
                decimal_places=2, default=1, max_digits=10, verbose_name="Total Amount"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="in_school",
            name="avail_status",
            field=models.CharField(
                choices=[("On Duty", "On Duty"), ("Off Duty", "Off Duty")],
                default=1,
                max_length=50,
                verbose_name="Availability Status",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="in_school",
            name="l_name",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.CASCADE,
                to="daystarapp.sitter",
                verbose_name="Name of Sitter",
            ),
        ),
        migrations.AlterField(
            model_name="sitter",
            name="dob",
            field=models.DateField(null=True, verbose_name="Date of Birth"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="educ_level",
            field=models.CharField(
                choices=[
                    ("Certificate", "Certificate"),
                    ("Diploma", "Diploma"),
                    ("Bachelors", "Bachelors"),
                    ("Masters", "Masters"),
                ],
                default=1,
                max_length=50,
                verbose_name="Level of Education",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="f_name",
            field=models.CharField(default=1, max_length=50, verbose_name="First Name"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="l_location",
            field=models.CharField(default=1, max_length=50, verbose_name="Location"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="l_name",
            field=models.CharField(default=1, max_length=50, verbose_name="Last Name"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="nin",
            field=models.CharField(
                default=1, max_length=50, verbose_name="National ID Number"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="nok",
            field=models.CharField(
                default=1,
                max_length=50,
                validators=[daystarapp.models.validate_two_names],
                verbose_name="Next of Kin",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="rec_contact",
            field=models.CharField(
                max_length=10,
                validators=[daystarapp.models.validate_phone_number],
                verbose_name="Recommender's Contact",
            ),
        ),
        migrations.AlterField(
            model_name="sitter",
            name="rec_name",
            field=models.CharField(
                default=1,
                max_length=50,
                validators=[daystarapp.models.validate_two_names],
                verbose_name="Recommender's Name",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="religion",
            field=models.CharField(
                choices=[
                    ("Christian", "Christian"),
                    ("Muslim", "Muslim"),
                    ("Hindu", "Hindu"),
                    ("Buddhist", "Buddhist"),
                    ("Jewish", "Jewish"),
                    ("Rather not say", "Rather not say"),
                ],
                default=1,
                max_length=50,
                verbose_name="Religious Affiliation",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="s_contact",
            field=models.CharField(
                default=1,
                max_length=10,
                validators=[daystarapp.models.validate_phone_number],
                verbose_name="Sitter's Contact",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitter",
            name="s_number",
            field=models.CharField(
                default=1,
                max_length=4,
                validators=[
                    daystarapp.models.validate_two_digit_integer,
                    django.core.validators.RegexValidator(
                        message="Value must be a two-digit integer", regex="^\\d{1,2}$"
                    ),
                ],
                verbose_name="Sitter Number",
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitterpayment",
            name="attendance_date",
            field=models.DateField(null=True, verbose_name="Date"),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="sitterpayment",
            name="l_name",
            field=models.ForeignKey(
                max_length=50,
                on_delete=django.db.models.deletion.CASCADE,
                to="daystarapp.sitter",
                verbose_name="Name of Sitter",
            ),
        ),
        migrations.AlterField(
            model_name="supply",
            name="consumed_today",
            field=models.CharField(
                default=1, max_length=20, verbose_name="Daily Comsumption"
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="supply",
            name="cost_per_item",
            field=models.DecimalField(
                decimal_places=2, default=1, max_digits=10, verbose_name="Cost Per Item"
            ),
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
        migrations.AlterField(
            model_name="supply",
            name="qty_stocked",
            field=models.CharField(
                default=1, max_length=20, verbose_name="Quantity Stocked"
            ),
            preserve_default=False,
        ),
    ]

# Generated by Django 5.0.4 on 2024-04-24 12:03

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("daystarapp", "0006_babyfee_alter_categorystay_name_and_more"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="baby",
            name="category",
        ),
        migrations.RemoveField(
            model_name="babyfee",
            name="gender",
        ),
        migrations.AddField(
            model_name="babyfee",
            name="category",
            field=models.ForeignKey(
                blank=True,
                choices=[
                    ("Morning", "Morning"),
                    ("Afternoon", "Afternoon"),
                    ("Evening", "Evening"),
                    ("Whole Day", "Whole Day"),
                ],
                null=True,
                on_delete=django.db.models.deletion.CASCADE,
                to="daystarapp.categorystay",
            ),
        ),
        migrations.AlterField(
            model_name="babyfee",
            name="payment_method",
            field=models.CharField(
                blank=True,
                choices=[
                    ("Cash", "Cash"),
                    ("Cheque", "Cheque"),
                    ("Mobile Money", "Mobile Money"),
                    ("Bank Transfer", "Bank Transfer"),
                ],
                max_length=50,
                null=True,
            ),
        ),
    ]

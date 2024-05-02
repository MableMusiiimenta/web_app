from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User
from django.core.validators import RegexValidator
from django.core.exceptions import ValidationError
import re
# Create your models here.

def validate_two_names(value):
    parts = value.strip().split()
    if len(parts) != 2:
        raise ValidationError('Please enter both first name and last name.')

class Index(models.Model):
    username = models.CharField(max_length=50, verbose_name="Administrator's Name", validators=[validate_two_names])
    password = models.CharField(max_length=50, verbose_name="Admin Password")

STAY = (
    ('Morning', 'Morning'),
    ('Afternoon', 'Afternoon'),
    ('Evening', 'Evening'),
    ('Whole Day', 'Whole Day'),
)
class Categorystay(models.Model):
    name = models.CharField(max_length=50, choices=STAY, null=True, blank=True)
    def __str__(self):
        return self.name

def validate_two_digit_integer(value):
    if not (value.isdigit() and 0 <= int(value) < 100):
        raise ValidationError('Value must be a two-digit integer')


def validate_phone_number(value):
    pattern = r'^\d{10}$'  # Regular expression for a 10-digit phone number
    if not re.match(pattern, value):
        raise ValidationError('Please enter a valid 10-digit phone number.')




class Baby(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    baby_number = models.CharField(max_length=4,null=True, blank=True, default=0, validators=[validate_two_digit_integer, RegexValidator(regex=r'^\d{1,2}$', message='Value must be a two-digit integer')])
    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=50, null=True, blank=True)
    parent_name = models.CharField(max_length=50, null=True, blank=True,validators=[validate_two_names])
    parent_contact = models.CharField(max_length=50, null=True, blank=True, validators=[validate_phone_number])
    def __str__(self):
        return f"Baby: {self.first_name} {self.last_name}"
    
RELIGION_CHOICES = (
    ('Christian', 'Christian'),
    ('Muslim', 'Muslim'),
    ('Hindu', 'Hindu'),
    ('Buddhist', 'Buddhist'),
    ('Jewish', 'Jewish'),
    ('Rather not say', 'Rather not say'),
)
EDUCATION_CHOICES = (
    ('Certificate', 'Certificate'),
    ('Diploma', 'Diploma'),
    ('Bachelors', 'Bachelors'),
    ('Masters', 'Masters'),
)
AVAILABILITY_STATUS = (
    ('On Duty', 'On Duty'),
    ('Off Duty', 'Off Duty'),
)

class Sitter(models.Model):
    f_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="First Name")
    l_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Last Name")
    l_location = models.CharField(max_length=50, null=True, blank=True, verbose_name="Location")
    dob = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    nok = models.CharField(max_length=50, null=True, blank=True, verbose_name="Next of Kin", validators=[validate_two_names])
    nin = models.CharField(max_length=50, null=True, blank=True, verbose_name="National ID Number")
    rec_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Recommender's Name", validators=[validate_two_names])
    rec_contact = models.CharField(max_length=10, blank=True, verbose_name="Recommender's Contact", validators=[validate_phone_number])
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES, null=True, blank=True, verbose_name="Religious Affiliation")
    educ_level = models.CharField(max_length=50, choices=EDUCATION_CHOICES, null=True, blank=True, verbose_name="Level of Education")
    s_number = models.CharField(max_length=4, null=True, blank=True, verbose_name="Sitter Number",validators=[validate_two_digit_integer, RegexValidator(regex=r'^\d{1,2}$', message='Value must be a two-digit integer')])
    s_contact = models.CharField(max_length=10, null=True, blank=True, verbose_name="Sitter's Contact", validators=[validate_phone_number])


    def __str__(self):
        return f"Sitter: {self.f_name} {self.l_name}"
    
PAYMENT_METHOD = (
    ('Cash', 'Cash'),
    ('Cheque', 'Cheque'),
    ('Mobile Money', 'Mobile Money'),
    ('Bank Transfer', 'Bank Transfer'),
)

class At_school(models.Model):
    arrival_time = models.DateTimeField(verbose_name="Time of Arrival")
    bringer_name = models.CharField(max_length=50,null=True, blank=True, verbose_name="Baby brought in by:", validators=[validate_two_names])
    period_of_stay = models.CharField(max_length=50, choices=STAY, null=True, blank=True)
    l_name = models.ForeignKey(Sitter,max_length=50, on_delete=models.CASCADE, blank=True, verbose_name="Assigned to Sitter")
    departure_time = models.DateTimeField(verbose_name="Time of Departure")
    taker_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Baby picked by:",validators=[validate_two_names])
    comment = models.CharField(max_length=100, null=True, blank=True, verbose_name="Comment")
    def __str__(self):
        return f"{self.l_name} - {self.arrival_time} - {self.departure_time}"
    
class In_school(models.Model):
    l_name = models.ForeignKey(Sitter,max_length=50, on_delete=models.CASCADE, blank=True, verbose_name="Name of Sitter")
    avail_status = models.CharField(max_length=50, choices=AVAILABILITY_STATUS, null=True, blank=True, verbose_name="Availability Status")
    babies_attd = models.ForeignKey(Baby, max_length=100, on_delete=models.CASCADE, verbose_name="Babies Assigned")
    payment = models.FloatField(verbose_name="Amount Paid to Sitter")

    def __str__(self):
        return f"{self.l_name} - {self.avail_status} - {self.babies_attd} - {self.payment}"


PAY_FOR = (
    ("Half-day", "Half-day"),
    ("Full-day", "Full-day"),
)

class Babyfee(models.Model):
    l_name = models.ForeignKey(Baby,max_length=100, on_delete=models.CASCADE, blank=True, verbose_name="For Baby")
    arrival_time = models.DateTimeField(verbose_name="Time of Arrival")
    departure_time = models.DateTimeField(verbose_name="Time of Departure")
    pay_for = models.CharField(max_length=20, null=True, choices=PAY_FOR, blank=True, verbose_name="Pay For")
    amount_due = models.DecimalField(max_digits=10, decimal_places=2, default=0, verbose_name="Amount Due")
    amount_paid = models.CharField(verbose_name="Price", max_length=7, blank=True, validators=[RegexValidator(r'^[0-9]+$')])
    payment_date = models.DateField(null=True, blank=True, verbose_name="Payment Date")
    payment_method = models.CharField(max_length=50, choices=PAYMENT_METHOD, null=True, blank=True, verbose_name="Mode of Payment")

    def save(self, *args, **kwargs):
        if self.pay_for == "Half-day":
            self.amount_due = 10000
        else:
            self.amount_due = 15000
        super(Babyfee, self).save(*args, **kwargs)
  


class SitterPayment(models.Model):
    l_name = models.ForeignKey(Sitter, on_delete=models.CASCADE, verbose_name="Name of Sitter", blank=True, max_length=50)
    attendance_date = models.DateField(null=True, blank=True, verbose_name="Date")
    number_of_babies = models.IntegerField(verbose_name="Number of Babies Attended To")
    payment_amount = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Amount Paid to Sitter")

    def calculate_payment_amount(self):
        amount_per_baby = 3000
        payment_amount = amount_per_baby * self.number_of_babies
        return payment_amount
    
    def save(self, *args, **kwargs):
        self.payment_amount = self.calculate_payment_amount()
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.l_name} - {self.attendance_date}"

class Supply(models.Model):
    item = models.CharField(max_length=100, verbose_name="Item")
    qty_stocked = models.CharField(max_length=20, null=True, blank=True, verbose_name="Quantity Stocked")
    cost_per_item = models.DecimalField(max_digits=10, decimal_places=2, null=True, verbose_name="Cost Per Item")
    total_cost = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Total Cost")
    date_stocked = models.DateField(null=True, blank=True, verbose_name="Date Stocked")
    qty_on_hand = models.CharField(max_length=20, verbose_name="Quantity In Stock")
    consumed_today = models.CharField(max_length=20, null=True, blank=True, verbose_name="Daily Comsumption")
    qty_left = models.CharField(max_length=20, verbose_name="Quantity Left")
    expiry_date = models.DateField(null=True, blank=True, verbose_name="Expiry Date")

    def __str__(self):
        return f"{self.item} - {self.qty_on_hand}"

class Doll(models.Model):
    name = models.CharField(max_length=100, verbose_name="Doll Name")
    brand = models.CharField(max_length=100, blank=True, null=True, verbose_name="Brand")
    color = models.CharField(max_length=50, blank=True, null=True, verbose_name="Color")
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Cost")
    qty_in_stock = models.IntegerField(verbose_name="Quantity in Stock")
    
    def __str__(self):
        return self.name
    
from django.db import models

class DollSale(models.Model):
    doll = models.ForeignKey(Doll, on_delete=models.CASCADE, verbose_name="Doll")
    sale_date = models.DateField(null=True, blank=True, verbose_name="Sale Date")
    l_name = models.ForeignKey(Baby, on_delete=models.CASCADE, blank=True, verbose_name="Sold To")
    price = models.CharField(verbose_name="Price", max_length=7, blank=True, validators=[RegexValidator(r'^[0-9]+$')])
    quantity_sold = models.PositiveIntegerField(null=True, blank=True, verbose_name="Quantity Sold")
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True, verbose_name="Total Amount")

    def save(self, *args, **kwargs):
        # Calculate total_amount before saving
        if self.price and self.quantity_sold:
            self.total_amount = float(self.price) * self.quantity_sold
        super().save(*args, **kwargs)








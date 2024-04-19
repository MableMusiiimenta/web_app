from django.db import models
from django.utils import timezone

# Create your models here.
class Categorystay(models.Model):
    name = models.CharField(max_length=50, null=True, blank=True)
    def __str__(self):
        return self.name


class Baby(models.Model):
    first_name = models.CharField(max_length=50, null=True, blank=True)
    last_name = models.CharField(max_length=50, null=True, blank=True)
    baby_number = models.PositiveIntegerField(null=True, blank=True, default=0)
    gender = models.CharField(max_length=10, null=True, blank=True)
    age = models.PositiveIntegerField()
    location = models.CharField(max_length=50, null=True, blank=True)
    parent_name = models.CharField(max_length=50, null=True, blank=True)
    bringer_name = models.CharField(max_length=50,null=True, blank=True)
    period_of_stay = models.CharField(max_length=50, null=True, blank=True)
    time_in = models.DateTimeField()
    fee_in_ugx = models.FloatField()
    taker_name = models.CharField(max_length=50, null=True, blank=True)
    time_out = models.DateTimeField()
    comment = models.CharField(max_length=100, null=True, blank=True)


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

class Sitter(models.Model):
    f_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="First Name")
    l_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Last Name")
    l_location = models.CharField(max_length=50, null=True, blank=True, verbose_name="Location")
    dob = models.DateField(null=True, blank=True, verbose_name="Date of Birth")
    nok = models.CharField(max_length=50, null=True, blank=True, verbose_name="Next of Kin")
    nin = models.CharField(max_length=50, null=True, blank=True, verbose_name="National ID Number")
    rec_name = models.CharField(max_length=50, null=True, blank=True, verbose_name="Recommender's Name")
    rec_contact = models.CharField(max_length=10, null=True, blank=True, verbose_name="Recommender's Contact")
    religion = models.CharField(max_length=50, choices=RELIGION_CHOICES, null=True, blank=True, verbose_name="Religious Affiliation")
    educ_level = models.CharField(max_length=50, null=True, blank=True, verbose_name="Level of Education")
    s_number = models.IntegerField(null=True, blank=True, verbose_name="Sitter Number")
    avail_status = models.CharField(max_length=50, null=True, blank=True, verbose_name="Availability Status")
    payment = models.FloatField(verbose_name="Amount Paid to Sitter")
    s_contact = models.IntegerField(null=True, blank=True, verbose_name="Sitter's Contact")


    def __str__(self):
        return f"Sitter: {self.f_name} {self.l_name}"




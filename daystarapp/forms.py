from django import forms
from .models import Baby
from .models import Sitter

class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ["first_name", "last_name", "baby_number", "gender", "age", "location", "parent_name", "bringer_name", "period_of_stay", "time_in", "fee_in_ugx", "taker_name", "time_out", "comment"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "baby_number": "Baby Number",
            "gender": "Gender",
            "age": "Age",
            "location": "Location",
            "parent_name": "Parent Name",
            "bringer_name": "Bringer Name",
            "period_of_stay": "Period of Stay",
            "time_in": "Time In",
            "fee_in_ugx": "Fee In UGX",
            "taker_name": "Taker Name",
            "time_out": "Time Out",
            "comment": "Comment",
        } 
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "baby_number": forms.NumberInput(attrs={"class": "form-control"}),
            "gender": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "parent_name": forms.TextInput(attrs={"class": "form-control"}),
            "bringer_name": forms.TextInput(attrs={"class": "form-control"}),
            "period_of_stay": forms.DateTimeInput(attrs={"class": "form-control"}),
            "time_in": forms.DateTimeInput(attrs={"class": "form-control"}),
            "fee_in_ugx": forms.NumberInput(attrs={"class": "form-control"}),
            "taker_name": forms.TextInput(attrs={"class": "form-control"}),
            "time_out": forms.DateTimeInput(attrs={"class": "form-control"}),
            "comment": forms.Textarea(attrs={"class": "form-control"}),
        }

# sitter form

class SitterForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = ["f_name", "l_name", "l_location", "dob", "nok", "nin", "rec_name", "rec_contact", "religion", "educ_level", "s_number", "avail_status", "payment", "s_contact"]
        labels = {
            "f_name": "First Name",
            "l_name": "Last Name",
            "l_location": "Location",
            "dob": "Date of Birth",
            "nok": "Next of Kin",
            "nin": "National ID Number",
            "rec_name": "Recommender's Name",
            "rec_contact": "Recommender's Contact",
            "religion": "Religion",
            "educ_level": "Level of Education",
            "s_number": "Sitter Number",
            "avail_status": "Availability Status",
            "payment": "Amount Paid to Sitter",
            "s_contact": "Sitter's Contact",
        } 
        widgets = {
            "f_name": forms.TextInput(attrs={"class": "form-control"}),
            "l_name": forms.TextInput(attrs={"class": "form-control"}),
            "l_location": forms.TextInput(attrs={"class": "form-control"}),
            "dob": forms.DateInput(attrs={"class": "form-control"}),
            "nok": forms.TextInput(attrs={"class": "form-control"}),
            "nin": forms.NumberInput(attrs={"class": "form-control"}),
            "rec_name": forms.TextInput(attrs={"class": "form-control"}),
            "rec_contact": forms.TextInput(attrs={"class": "form-control"}),
            "religion": forms.TextInput(attrs={"class": "form-control"}),
            "educ_level": forms.TextInput(attrs={"class": "form-control"}),
            "s_number": forms.NumberInput(attrs={"class": "form-control"}),
            "avail_status": forms.TextInput(attrs={"class": "form-control"}),
            "payment": forms.NumberInput(attrs={"class": "form-control"}),
            "s_contact": forms.NumberInput(attrs={"class": "form-control"}),
        }

            

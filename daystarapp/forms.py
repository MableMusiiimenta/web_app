from django import forms
from django.shortcuts import render, redirect
from .models import Baby
from .models import Sitter
from .models import Babyfee
from .models import SitterPayment
from .models import Supply
from .models import Doll
from .models import DollSale
from .models import At_school
from .models import In_school
from .models import Admin_login
from django.core.exceptions import ValidationError


class Admin_loginForm(forms.ModelForm):
    class Meta:
        model = Admin_login
        fields = ['username', 'email', 'password']
        labels = {
            "username": "Administrator's Name",
            "email": "Administrator's Email",
            "password": "Admin Password",
        }
        widgets = {
            "username": forms.TextInput(attrs={"class": "form-control", "placeholder": "Enter full name"}),
            "email": forms.EmailInput(attrs={"class": "form-control", "placeholder": "Enter email"}),
            "password": forms.PasswordInput(attrs={"class": "form-control", "placeholder": "Enter password"}),
        }
    def clean_username(self):
        value = self.cleaned_data["username"]
        parts = value.strip().split()
        if len(parts) != 2:
            raise forms.ValidationError("Please enter both first name and last name.")
        return value
    
    
class BabyForm(forms.ModelForm):
    class Meta:
        model = Baby
        fields = ["first_name", "last_name", "baby_number", "gender", "age", "location", "parent_name", "parent_contact"]
        labels = {
            "first_name": "First Name",
            "last_name": "Last Name",
            "baby_number": "Baby Number",
            "gender": "Gender",
            "age": "Age",
            "location": "Location",
            "parent_name": "Parent's Name",
            "parent_contact": "Parent's Contact",
          
        } 
        widgets = {
            "first_name": forms.TextInput(attrs={"class": "form-control"}),
            "last_name": forms.TextInput(attrs={"class": "form-control"}),
            "baby_number": forms.NumberInput(attrs={"class": "form-control"}),
            "gender": forms.TextInput(attrs={"class": "form-control"}),
            "age": forms.NumberInput(attrs={"class": "form-control"}),
            "location": forms.TextInput(attrs={"class": "form-control"}),
            "parent_name": forms.TextInput(attrs={"class": "form-control"}),
            "parent_contact": forms.TextInput(attrs={"class": "form-control"}),
        }

# sitter form

class SitterForm(forms.ModelForm):
    class Meta:
        model = Sitter
        fields = ["f_name", "l_name", "l_location", "dob", "nok", "nin", "rec_name", "rec_contact", "religion", "educ_level", "s_number", "s_contact"]
        labels = {
            "f_name": "First Name",
            "l_name": "Last Name",
            "l_location": "Location",
            "dob": "Date of Birth",
            "nok": "Next of Kin",
            "nin": "National ID Number",
            "rec_name": "Recommender's Name",
            "rec_contact": "Recommender's Phone Number",
            "religion": "Religion",
            "educ_level": "Level of Education",
            "s_number": "Sitter Number",
            "s_contact": "Sitter's Phone Number",
        } 
        widgets = {
            "f_name": forms.TextInput(attrs={"class": "form-control"}),
            "l_name": forms.TextInput(attrs={"class": "form-control"}),
            "l_location": forms.TextInput(attrs={"class": "form-control"}),
            "dob": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "nok": forms.TextInput(attrs={"class": "form-control"}),
            "nin": forms.TextInput(attrs={"class": "form-control"}),
            "rec_name": forms.TextInput(attrs={"class": "form-control"}),
            "contact": forms.TextInput(attrs={"class": "form-control", "type":"number"}),
            "reli": forms.TextInput(attrs={"class": "form-control"}),
            "educ": forms.TextInput(attrs={"class": "form-control"}),
            "number": forms.NumberInput(attrs={"class": "form-control"}),
            "contact": forms.TextInput(attrs={"class": "form-control", "type":"number"}),
        }

class At_schoolForm(forms.ModelForm):
    class Meta:
        model =At_school
        fields = ["arrival_time", "bringer_name", "period_of_stay", "l_name", "departure_time", "taker_name", "comment"]
        labels = {
            "arrival_time": "Time of Arrival",
            "bringer_name": "Bringer's Name",
            "period_of_stay": "Period of Stay",
            "l_name": "Assigned to Sitter",
            "departure_time": "Time of Departure",
            "taker_name": "Baby picked by",
            "comment": "Comment",
        }
        widgets = {
            "arrival_time": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "bringer_name": forms.TextInput(attrs={"class": "form-control"}),
            "stay": forms.TextInput(attrs={"class": "form-control"}),
            "assigned": forms.TextInput(attrs={"class": "form-control"}),
            "departure_time": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "taker_name": forms.TextInput(attrs={"class": "form-control"}),
            "comment": forms.TextInput(attrs={"class": "form-control"}),
        }

class BabyfeeForm(forms.ModelForm):
    class Meta:
        model = Babyfee
        fields = ["l_name", "arrival_time", "departure_time", "pay_for", "amount_due", "amount_paid", "payment_date", "payment_method"]
        labels = {
            "l_name": "For",
            "arrival_time": "Time In",
            "departure_time": "Time Out",
            "pay_for": "Pay For",
            "amount_due": "Amount Due",
            "amount_paid": "Amount Paid",
            "payment_date": "Date of Payment",
            "payment_method": "Mode of Payment",
        
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "arrival_time": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "departure_time": forms.DateTimeInput(attrs={"class": "form-control", "type": "datetime-local"}),
            "for": forms.TextInput(attrs={"class": "form-control"}),
            "due": forms.NumberInput(attrs={"class": "form-control"}),
            "paid": forms.NumberInput(attrs={"class": "form-control"}),
            "payment_date": forms.DateInput(attrs={"class": "form-control", "type":"date"}),
            "method": forms.TextInput(attrs={"class": "form-control"}),
            
        }

class SitterPaymentForm(forms.ModelForm):
    class Meta:
        model = SitterPayment
        fields = ["l_name", "attendance_date", "number_of_babies", "payment_amount"]
        labels = {
            "l_name": "Name of Sitter",
            "attendance_date": "Attendance Date",
            "number_of_babies": "Number of Babies Attended To",
            "payment_amount": "Amount Paid to Sitter",
        } 
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "attendance_date": forms.DateInput(attrs={"class": "form-control", "type":"date"}),
            "number_of_babies": forms.NumberInput(attrs={"class": "form-control"}),
            "payment_amount": forms.NumberInput(attrs={"class": "form-control"}),
        }
class SupplyForm(forms.ModelForm):
    class Meta:
        model = Supply
        fields = ["item", "qty_stocked", "cost_per_item", "total_cost", "date_stocked", "qty_on_hand", "consumed_today", "qty_left", "expiry_date"]
        labels = {
            "item": "Item",
            "qty_stocked": "Quantity Stocked",
            "cost_per_item": "Cost Per Item",
            "total_cost": "Total Cost",
            "date_stocked": "Date Stocked",
            "qty_on_hand": "Quantity In Stock",
            "consumed_today": "Consumed Today",
            "qty_left": "Quantity Left",
            "expiry_date": "Expiry Date",
        }
        widgets = {
            "item": forms.TextInput(attrs={"class": "form-control"}),
            "stocked": forms.NumberInput(attrs={"class": "form-control"}),
            "cost_per_item": forms.TextInput(attrs={"class": "form-control", "type": "number"}),
            "total_cost": forms.TextInput(attrs={"class": "form-control", "type": "number"}),
            "date_stocked": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "qty_on_hand": forms.NumberInput(attrs={"class": "form-control"}),
            "consumed_today": forms.NumberInput(attrs={"class": "form-control"}),
            "qty_left": forms.NumberInput(attrs={"class": "form-control"}),
            "expiry_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
        }

class DollForm(forms.ModelForm):
    class Meta:
        model = Doll
        fields = ["name", "brand", "color", "price", "qty_in_stock"]
        labels = {
            "name": "Doll Name",
            "brand": "Brand",
            "color": "Color",
            "price": "Cost",
            "qty_in_stock": "Quantity in Stock",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "brand": forms.TextInput(attrs={"class": "form-control"}),
            "color": forms.TextInput(attrs={"class": "form-control"}),
            "price": forms.NumberInput(attrs={"class": "form-control"}),
            "qty_in_stock": forms.NumberInput(attrs={"class": "form-control"}),
        }

class DollSaleForm(forms.ModelForm):
    class Meta:
        model = DollSale
        fields = ["doll", "sale_date", "l_name", "price", "quantity_sold", "total_amount"]
        labels = {
            "doll": "Doll",
            "sale_date": "Sale Date",
            "l_name": "Sold To",
            "price": "Price",
            "quantity_sold": "Quantity Sold",
            "total_amount": "Total Amount",
        }
        widgets = {
            "name": forms.TextInput(attrs={"class": "form-control"}),
            "sale_date": forms.DateInput(attrs={"class": "form-control", "type": "date"}),
            "sold_to": forms.TextInput(attrs={"class": "form-control"}),
            "cost": forms.TextInput(attrs={"class": "form-control", "type": "number"}),
            "quantity_sold": forms.NumberInput(attrs={"class": "form-control"}),
            "total_amount": forms.TextInput(attrs={"class": "form-control", "type": "number"}),
        }

class In_schoolForm(forms.ModelForm):
    class Meta:
        model = In_school
        fields = ["l_name", "avail_status", "babies_attd", "payment"]
        labels = {
            "l_name": "Name of Sitter",
            "avail_status": "Availability Status",
            "babies_attd": "Babies Assigned",
            "payment": "Amount Paid to Sitter",
        }
        widgets = {
            "sitter": forms.TextInput(attrs={"class": "form-control"}),
            "avail": forms.TextInput(attrs={"class": "form-control"}),
            "assigned": forms.TextInput(attrs={"class": "form-control"}),
            "payment": forms.TextInput(attrs={"class": "form-control"}),
        }

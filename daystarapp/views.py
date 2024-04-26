from django.http import HttpResponseRedirect
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse

from .models import Baby
from .forms import BabyForm
from .models import Sitter, SitterPayment
from.forms import SitterForm
from .forms import SitterPaymentForm
from .models import In_school
from .models import Babyfee
from .forms import BabyfeeForm
from .models import At_school
from .forms import At_schoolForm
from .forms import In_schoolForm
from .models import Supplies
from .forms import SuppliesForm
from .models import Doll, DollSale
from .forms import DollForm
from .forms import DollSaleForm




# Create your views here.





def index(request):
    
    images = [
        '/static/images/badge.png',
        '/static/images/two.jpg',
        '/static/images/sitting.jpg',
        '/static/images/play.jpg',
        '/static/images/dimple.jpg',
    ]
    return render(request, 'index.html', {'images': images})

def board(request):
    return render(request, 'board.html')

def dashb(request):
    return render(request, 'dashb.html')
def serve_js(request):
    with open('static/script.js', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/javascript')
    return response

def baby(request):
    return render(request, "babies/baby.html", {"babies": Baby.objects.all()} )

def view_baby(request, id):
    baby = Baby.objects.get(pk=id)
    return HttpResponseRedirect(reverse("baby"))


def add(request):
    if request.method == "POST":
        form = BabyForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data["first_name"]
            new_last_name = form.cleaned_data["last_name"]
            new_baby_number = form.cleaned_data["baby_number"]
            new_age = form.cleaned_data["age"]
            new_location = form.cleaned_data["location"]
            new_parent_name = form.cleaned_data["parent_name"]
            new_parent_contact = form.cleaned_data["parent_contact"]
       

            new_baby = Baby(
                first_name=new_first_name,
                last_name=new_last_name,
                baby_number=new_baby_number,
                age=new_age,
                location=new_location,
                parent_name=new_parent_name,
                parent_contact=new_parent_contact,
            )
            new_baby.save()
            return render(request, "babies/add.html", {
                "form": BabyForm(),
                "success": True
            })
    else:
        form = BabyForm()

    return render(request, "babies/add.html", {
        "form": form
    })

def edit(request, id):
    if request.method == "POST":
        baby = Baby.objects.get(pk=id)
        form = BabyForm(request.POST, instance=baby)
        if form.is_valid():
            form.save()
            return render(request, "babies/edit.html", {
                "form": form,
                "success": True
            })
    else:
        baby = Baby.objects.get(pk=id)
        form = BabyForm(instance=baby)
    return render(request, "babies/edit.html", {
            "form": form
        })

def delete(request, id):
    if request.method == "POST":
        baby = Baby.objects.get(pk=id)
        baby.delete()
    return HttpResponseRedirect(reverse("baby"))


# Sitter view

def sitter(request):
    return render(request, "sitters/sitter.html", {"sitters": Sitter.objects.all()} )

def view_sitter(request, id):
    sitter = Sitter.objects.get(pk=id)
    return HttpResponseRedirect(reverse("sitter"))

def adds(request):
    if request.method == "POST":
        form = SitterForm(request.POST)
        if form.is_valid():
            new_f_name = form.cleaned_data["f_name"]
            new_l_name = form.cleaned_data["l_name"]
            new_l_location = form.cleaned_data["l_location"]
            new_rec_name = form.cleaned_data["rec_name"]
            new_rec_contact = form.cleaned_data["rec_contact"]
            new_religion = form.cleaned_data["religion"]
            new_educ_level = form.cleaned_data["educ_level"]
            new_s_number = form.cleaned_data["s_number"]
            new_s_contact = form.cleaned_data["s_contact"]

            new_sitter = Sitter(
                f_name=new_f_name,
                l_name=new_l_name,
                l_location=new_l_location,
                rec_name=new_rec_name,
                rec_contact=new_rec_contact,
                religion=new_religion,
                educ_level=new_educ_level,
                s_number=new_s_number,
                s_contact=new_s_contact
            )
            new_sitter.save()
            return render(request, "sitters/adds.html", {
                "form": SitterForm(),
                "success": True
            })
    else:
        form = SitterForm()

    return render(request, "sitters/adds.html", {
        "form": form
    })

def edits(request, id):
    if request.method == "POST":
        sitter = Sitter.objects.get(pk=id)
        form = SitterForm(request.POST, instance=sitter)
        if form.is_valid():
            form.save()
            return render(request, "sitters/edits.html", {
                "form": form,
                "success": True
            })
    else:
        sitter = Sitter.objects.get(pk=id)
        form = SitterForm(instance=sitter)
    return render(request, "sitters/edits.html", {
            "form": form
        })

def deletes(request, id):
    if request.method == "POST":
        sitter = Sitter.objects.get(pk=id)
        sitter.delete()
    return HttpResponseRedirect(reverse("sitter"))

def calculate_payment(request, baby_id):
    baby = Baby.objects.get(id=baby_id)
    baby.calculate_payment()
    baby.save()
    return render(request, 'payment_confirmation.html', {'baby': baby})

def view_payment_history(request):
    payments = Baby.objects.filter(payment_date__isnull=False)
    return render(request, 'payment_history.html', {'payments': payments})

def handle_monthly_payments(request):
    return render(request, 'monthly_payments.html')

def handle_sitter_payment(request, sitter_id):
    if request.method == 'POST':
        attendance_date = request.POST.get('attendance_date')
        number_of_babies = int(request.POST.get('number_of_babies'))
        sitter = Sitter.objects.get(id=sitter_id)
        
        # Calculate payment amount
        payment_amount = number_of_babies * 3000
        
        # Create a new SitterPayment instance and save it
        sitter_payment = SitterPayment(sitter=sitter, attendance_date=attendance_date, number_of_babies=number_of_babies, payment_amount=payment_amount)
        sitter_payment.save()
        
        # Redirect to a confirmation page
        return redirect('payment_confirmation', payment_id=sitter_payment.id)
    else:
        # Handle GET request (display the form)
        sitter = Sitter.objects.get(id=sitter_id)
        return render(request, 'sitter_payment_form.html', {'sitter': sitter})
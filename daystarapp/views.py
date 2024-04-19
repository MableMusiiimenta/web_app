from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse

from .models import Baby
from .forms import BabyForm

from .models import Sitter
from.forms import SitterForm


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
            new_bringer_name = form.cleaned_data["bringer_name"]
            new_period_of_stay = form.cleaned_data["period_of_stay"]
            new_time_in = form.cleaned_data["time_in"]
            new_fee_in_ugx = form.cleaned_data["fee_in_ugx"]
            new_taker_name = form.cleaned_data["taker_name"]
            new_time_out = form.cleaned_data["time_out"]
            new_comment = form.cleaned_data["comment"]

            new_baby = Baby(
                first_name=new_first_name,
                last_name=new_last_name,
                baby_number=new_baby_number,
                age=new_age,
                location=new_location,
                parent_name=new_parent_name,
                bringer_name=new_bringer_name,
                period_of_stay=new_period_of_stay,
                time_in=new_time_in,
                fee_in_ugx=new_fee_in_ugx,
                taker_name=new_taker_name,
                time_out=new_time_out,
                comment=new_comment
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
            new_avail_status = form.cleaned_data["avail_status"]
            new_payment = form.cleaned_data["payment"]
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
                avail_status=new_avail_status,
                payment=new_payment,
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


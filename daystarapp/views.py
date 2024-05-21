from django.http import HttpResponseRedirect
from django.http import HttpResponseBadRequest
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.urls import reverse
from django.contrib.auth.models import User
from .forms import Admin_loginForm
from django.contrib.auth.decorators import login_required
from .models import Baby
from .forms import BabyForm
from .models import Sitter, SitterPayment
from.forms import SitterForm
from .forms import SitterPaymentForm
from .models import Shift
from .models import Babyfee
from .forms import BabyfeeForm
from .models import Monthlyfee
from .forms import MonthlyfeeForm
from .models import At_school
from .forms import At_schoolForm
from .forms import ShiftForm
from .models import Supply
from .forms import SupplyForm
from .models import Doll, DollSale
from .forms import DollForm
from .forms import DollSaleForm
from django.contrib.auth import authenticate, login
from django.contrib.auth import logout
from django.db.models import Sum

# Create your views here.
    
def index(request):
    
    images = [
        '/static/images/two.jpg',
        '/static/images/play.jpg',
    ]
    return render(request, 'index.html', {'images': images})



def admin_login(request):
    if request.method == 'POST':
        form = Admin_loginForm(request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']

            # Authenticate user
            user = authenticate(request, username=username, password=password)
            if user is not None:
                # Log the user in
                login(request, user)
                return redirect('dashb')  # Redirect to dashboard on successful login
            else:
                # Add error message for incorrect credentials
                form.add_error(None, "Invalid username or password.")
    else:
        form = Admin_loginForm()

    # If the form is not valid or it's a GET request, render the form template
    return render(request, 'admin_login.html', {'form': form})





@login_required
def dashb(request):
    total_babies = Baby.objects.count()
    # Pass the count to the template
    total_fees = Babyfee.objects.aggregate(total_fees=Sum("amount_paid"))["total_fees"] or 0

    return render(request, 'dashb.html', {'total_babies': total_babies, 'total_fees': total_fees})
def serve_js(request):
    with open('static/script.js', 'rb') as f:
        response = HttpResponse(f.read(), content_type='application/javascript')
    return response

def search_results(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    results = Baby.objects.filter(first_name__icontains=query) |  Baby.objects.filter(last_name__icontains=query)# Filter records based on the query
    return render(request, 'search_results.html', {'results': results, 'query': query})

def search_another_model(request):
    query = request.GET.get('q', '')  # Get the search query from the request
    results = Sitter.objects.filter(field__icontains=query) |  Sitter.objects.filter(last_name__icontains=query)  # Adjust filtering criteria based on your model
    return render(request, 'search_another_model.html', {'results': results, 'query': query})

@login_required
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
# At_school
@login_required
def at_school(request):
    return render(request, "at_schools/at_school.html", {"at_schools": At_school.objects.all()} )

def view_at_school(request, id):
    at_school = At_school.objects.get(pk=id)
    return HttpResponseRedirect(reverse("at_school"))

def addd(request):
    if request.method == "POST":
        form = At_schoolForm(request.POST)
        if form.is_valid():
            new_first_name = form.cleaned_data["first_name"]
            new_arrival_time = form.cleaned_data["arrival_time"]
            new_bringer_name = form.cleaned_data["bringer_name"]
            new_period_of_stay = form.cleaned_data["period_of_stay"]
            new_l_name = form.cleaned_data["l_name"]
            new_departure_time = form.cleaned_data["departure_time"]
            new_taker_name = form.cleaned_data["taker_name"]
            new_comment = form.cleaned_data["comment"]
       

            new_at_school = At_school(
                first_name=new_first_name,
                arrival_time=new_arrival_time,
                bringer_name=new_bringer_name,
                period_of_stay=new_period_of_stay,
                l_name=new_l_name,
                departure_time=new_departure_time,
                taker_name=new_taker_name,
                comment=new_comment,
            )
            new_at_school.save()
            return render(request, "at_schools/addd.html", {
                "form": At_schoolForm(),
                "success": True
            })
    else:
        form = At_schoolForm()

    return render(request, "at_schools/addd.html", {
        "form": form
    })

def editt(request, id):
    if request.method == "POST":
        at_school = At_school.objects.get(pk=id)
        form = At_schoolForm(request.POST, instance=at_school)
        if form.is_valid():
            form.save()
            return render(request, "at_schools/editt.html", {
                "form": form,
                "success": True
            })
    else:
        at_school = At_school.objects.get(pk=id)
        form = At_schoolForm(instance=at_school)
    return render(request, "at_schools/editt.html", {
            "form": form
        })

def deletee(request, id):
    if request.method == "POST":
        at_school = At_school.objects.get(pk=id)
        at_school.delete()
    return HttpResponseRedirect(reverse("at_school"))



#shift view

@login_required
def shift(request):
    shifts = Shift.objects.all()

    for shift in shifts:
        shift.babies_assigned = shift.count_assigned_babies()

    # Pass the list of shifts and total count of assignments for each sitter to the template
    return render(request, "shifts/shift.html", {'shifts': shifts})

def view_shift(request, id):
    shift = Shift.objects.get(pk=id)
    return HttpResponseRedirect(reverse("shift"))

def adddd(request):
    if request.method == "POST":
        form = ShiftForm(request.POST)
        if form.is_valid():
            new_l_name = form.cleaned_data["l_name"]
            new_date = form.cleaned_data["date"]
            new_period = form.cleaned_data["period"]
            new_start_time = form.cleaned_data["start_time"]
            new_end_time = form.cleaned_data["end_time"]
            new_babies_assigned = form.cleaned_data["babies_assigned"]

            new_shift = Shift(
                l_name=new_l_name,
                date=new_date,
                period=new_period,
                start_time=new_start_time,
                end_time=new_end_time,
                babies_assigned=new_babies_assigned,
            )
            new_shift.save()
            return render(request, "shifts/adddd.html", {
                "form": ShiftForm(),
                "success": True
            })
    else:
        form = ShiftForm()

    return render(request, "shifts/adddd.html", {
        "form": form
    })

def edittt(request, id):
    if request.method == "POST":
        shift = Shift.objects.get(pk=id)
        form = ShiftForm(request.POST, instance=shift)
        if form.is_valid():
            form.save()
            return render(request, "shifts/edittt.html", {
                "form": form,
                "success": True
            })
    else:
        shift = Shift.objects.get(pk=id)
        form = ShiftForm(instance=shift)
    return render(request, "shifts/edittt.html", {
            "form": form
        })

def deleteee(request, id):
    if request.method == "POST":
        shift = Shift.objects.get(pk=id)
        shift.delete()
    return HttpResponseRedirect(reverse("shift"))

@login_required
def supply(request):
    return render(request, "supplies/supply.html", {"supplies": Supply.objects.all()} )

def view_supply(request, id):
    supply = Supply.objects.get(pk=id)
    return HttpResponseRedirect(reverse("supply"))


def addds(request):
    if request.method == "POST":
        form = SupplyForm(request.POST)
        if form.is_valid():
            new_date_of_today = form.cleaned_data["date_of_today"]
            new_item = form.cleaned_data["item"]
            new_qty_stocked = form.cleaned_data["qty_stocked"]
            new_cost_per_item = form.cleaned_data["cost_per_item"]
            new_total_cost = form.cleaned_data["total_cost"]
            new_date_stocked = form.cleaned_data["date_stocked"]
            new_qty_on_hand = form.cleaned_data["qty_on_hand"]
            new_consumed_today = form.cleaned_data["consumed_today"]
            new_qty_left = form.cleaned_data["qty_left"]
            new_expiry_date = form.cleaned_data["expiry_date"]
       

            new_supply = Supply(
                date_of_today=new_date_of_today,
                item=new_item,
                qty_stocked=new_qty_stocked,
                cost_per_item=new_cost_per_item,
                total_cost=new_total_cost,
                date_stocked=new_date_stocked,
                qty_on_hand=new_qty_on_hand,
                consumed_today=new_consumed_today,
                qty_left=new_qty_left,
                expiry_date=new_expiry_date,
            )
            new_supply.save()
            return render(request, "supplies/addds.html", {
                "form": SupplyForm(),
                "success": True
            })
    else:
        form = SupplyForm()

    return render(request, "supplies/addds.html", {
        "form": form
    })

def editts(request, id):
    if request.method == "POST":
        supply = Supply.objects.get(pk=id)
        form = SupplyForm(request.POST, instance=supply)
        if form.is_valid():
            form.save()
            return render(request, "supplies/editts.html", {
                "form": form,
                "success": True
            })
    else:
        supply = Supply.objects.get(pk=id)
        form = SupplyForm(instance=supply)
    return render(request, "supplies/editts.html", {
            "form": form
        })

def deletees(request, id):
    if request.method == "POST":
        supply = Supply.objects.get(pk=id)
        supply.delete()
    return HttpResponseRedirect(reverse("supply"))


@login_required
def doll(request):
    return render(request, "dolls/doll.html", {"dolls": Doll.objects.all()} )

def view_doll(request, id):
    doll = Doll.objects.get(pk=id)
    return HttpResponseRedirect(reverse("doll"))


def adddds(request):
    if request.method == "POST":
        form = DollForm(request.POST)
        if form.is_valid():
            new_name = form.cleaned_data["name"]
            new_brand = form.cleaned_data["brand"]
            new_color = form.cleaned_data["color"]
            new_qty_stocked = form.cleaned_data["quantity_stocked"]
            new_stock_date = form.cleaned_data["stock_date"]
            new_buying_price = form.cleaned_data["buying_price"]
            new_price = form.cleaned_data["price"]
            new_qty_in_stock = form.cleaned_data["qty_in_stock"]
            new_qty_left = form.cleaned_data["qty_left"]

            new_doll = Doll(
                name=new_name,
                brand=new_brand,
                color=new_color,
                qty_stocked=new_qty_stocked,
                stock_date=new_stock_date,
                buying_price=new_buying_price,
                price=new_price,
                qty_in_stock=new_qty_in_stock,
                qty_left=new_qty_left,
            )
            new_doll.save()
            return render(request, "dolls/adddds.html", {
                "form": DollForm(),
                "success": True
            })
    else:
        form = DollForm()

    return render(request, "dolls/adddds.html", {
        "form": form
    })

def edittts(request, id):
    if request.method == "POST":
        doll = Doll.objects.get(pk=id)
        form = DollForm(request.POST, instance=doll)
        if form.is_valid():
            form.save()
            return render(request, "dolls/edittts.html", {
                "form": form,
                "success": True
            })
    else:
        doll = Doll.objects.get(pk=id)
        form = DollForm(instance=doll)
    return render(request, "dolls/edittts.html", {
            "form": form
        })

def deleteees(request, id):
    if request.method == "POST":
        doll = Doll.objects.get(pk=id)
        doll.delete()
    return HttpResponseRedirect(reverse("doll"))


@login_required
def dollsale(request):
    return render(request, "dollsales/dollsale.html", {"dollsales": DollSale.objects.all()} )

def view_dollsale(request, id):
    dollsale = DollSale.objects.get(pk=id)
    return HttpResponseRedirect(reverse("dollsale"))


def addddd(request):
    if request.method == "POST":
        form = DollSaleForm(request.POST)
        if form.is_valid():
            new_doll = form.cleaned_data["doll"]
            new_sale_date = form.cleaned_data["sale_date"]
            new_l_name = form.cleaned_data["l_name"]
            new_price = form.cleaned_data["price"]
            new_quantity_sold = form.cleaned_data["quantity_sold"]
            new_total_amount = form.cleaned_data["total_amount"]
          
            new_dollsale = DollSale(
                doll=new_doll,
                sale_date=new_sale_date,
                l_name=new_l_name,
                price=new_price,
                quantity_sold=new_quantity_sold,
                total_amount=new_total_amount,
            )
            new_dollsale.save()
            return render(request, "dollsales/addddd.html", {
                "form": DollSaleForm(),
                "success": True
            })
    else:
        form = DollSaleForm()

    return render(request, "dollsales/addddd.html", {
        "form": form
    })

def editttt(request, id):
    if request.method == "POST":
        dollsale = DollSale.objects.get(pk=id)
        form = DollSaleForm(request.POST, instance=dollsale)
        if form.is_valid():
            form.save()
            return render(request, "dollsales/editttt.html", {
                "form": form,
                "success": True
            })
    else:
        dollsale = DollSale.objects.get(pk=id)
        form = DollSaleForm(instance=dollsale)
    return render(request, "dollsales/editttt.html", {
            "form": form
        })

def deleteeee(request, id):
    if request.method == "POST":
        doll = DollSale.objects.get(pk=id)
        doll.delete()
    return HttpResponseRedirect(reverse("dollsale"))


# Sitter view
@login_required
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


@login_required
def babyfee(request):
    return render(request, "babyfees/babyfee.html", {"babyfees": Babyfee.objects.all()} )

def view_babyfee(request, id):
    babyfee = Babyfee.objects.get(pk=id)
    return HttpResponseRedirect(reverse("babyfee"))

def adi(request):
    if request.method == "POST":
        form = BabyfeeForm(request.POST)
        if form.is_valid():
            new_l_name = form.cleaned_data["l_name"]
            new_arrival_time = form.cleaned_data["arrival_time"]
            new_departure_time = form.cleaned_data["departure_time"]
            new_pay_for = form.cleaned_data["pay_for"]
            new_amount_due = form.cleaned_data["amount_due"]
            new_amount_paid = form.cleaned_data["amount_paid"]
            new_pending_amount = form.cleaned_data["pending_amount"]
            new_payment_date = form.cleaned_data["payment_date"]
            new_payment_method = form.cleaned_data["payment_method"]

            new_babyfee = Babyfee(
                l_name=new_l_name,
                arrival_time=new_arrival_time,
                departure_time=new_departure_time,
                pay_for=new_pay_for,
                amount_due=new_amount_due,
                amount_paid=new_amount_paid,
                pending_amount=new_pending_amount,
                payment_date=new_payment_date,
                payment_method=new_payment_method
                
            )
            new_babyfee.save()
            return render(request, "babyfees/adi.html", {
                "form": BabyfeeForm(),
                "success": True
            })
    else:
        form = BabyfeeForm()

    return render(request, "babyfees/adi.html", {
        "form": form
    })

def edi(request, id):
    if request.method == "POST":
        babyfee = Babyfee.objects.get(pk=id)
        form = BabyfeeForm(request.POST, instance=babyfee)
        if form.is_valid():
            form.save()
            return render(request, "babyfees/edi.html", {
                "form": form,
                "success": True
            })
    else:
        babyfee = Babyfee.objects.get(pk=id)
        form = BabyfeeForm(instance=babyfee)
    return render(request, "babyfees/edi.html", {
            "form": form
        })

def dele(request, id):
    if request.method == "POST":
        babyfee = Babyfee.objects.get(pk=id)
        babyfee.delete()
    return HttpResponseRedirect(reverse("babyfee"))

@login_required
def monthlyfee(request):
    return render(request, "monthlyfees/monthlyfee.html", {"monthlyfees": Monthlyfee.objects.all()} )

def view_monthlyfee(request, id):
    monthlyfee = Monthlyfee.objects.get(pk=id)
    return HttpResponseRedirect(reverse("monthlyfee"))

def addt(request):
    if request.method == "POST":
        form = MonthlyfeeForm(request.POST)
        if form.is_valid():
            new_l_name = form.cleaned_data["l_name"]
            new_pay_for = form.cleaned_data["pay_for"]
            new_amount_due = form.cleaned_data["amount_due"]
            new_amount_paid = form.cleaned_data["amount_paid"]
            new_pending_amount = form.cleaned_data["pending_amount"]
            new_payment_date = form.cleaned_data["payment_date"]
            new_payment_method = form.cleaned_data["payment_method"]

            new_monthlyfee = Monthlyfee(
                l_name=new_l_name,
                pay_for=new_pay_for,
                amount_due=new_amount_due,
                amount_paid=new_amount_paid,
                pending_amount=new_pending_amount,
                payment_date=new_payment_date,
                payment_method=new_payment_method
                
            )
            new_monthlyfee.save()
            return render(request, "monthlyfees/addt.html", {
                "form": MonthlyfeeForm(),
                "success": True
            })
    else:
        form = MonthlyfeeForm()

    return render(request, "monthlyfees/addt.html", {
        "form": form
    })

def eddt(request, id):
    if request.method == "POST":
        monthlyfee = Monthlyfee.objects.get(pk=id)
        form = MonthlyfeeForm(request.POST, instance=monthlyfee)
        if form.is_valid():
            form.save()
            return render(request, "monthlyfees/eddt.html", {
                "form": form,
                "success": True
            })
    else:
        monthlyfee = Monthlyfee.objects.get(pk=id)
        form = MonthlyfeeForm(instance=monthlyfee)
    return render(request, "monthlyfees/eddt.html", {
            "form": form
        })

def delet(request, id):
    if request.method == "POST":
        monthlyfee = Monthlyfee.objects.get(pk=id)
        monthlyfee.delete()
    return HttpResponseRedirect(reverse("monthlyfee"))



@login_required
def sitterpayment(request):
    sitterpayments = SitterPayment.objects.all()

    return render(request, "sitterpayments/sitterpayment.html", {"sitterpayments": sitterpayments} )

def view_sitterpayment(request, id):
    sitterpayment = SitterPayment.objects.get(pk=id)
    return HttpResponseRedirect(reverse("sitterpayment"))

def addi(request):
    if request.method == "POST":
        form = SitterPaymentForm(request.POST)
        if form.is_valid():
            new_l_name = form.cleaned_data["l_name"]
            new_attendance_date = form.cleaned_data["attendance_date"]
            new_payment_amount = form.cleaned_data["payment_amount"]
            

            new_sitterpayment = SitterPayment(
                l_name=new_l_name,
                attendance_date=new_attendance_date,
                payment_amount=new_payment_amount
                
            )
            new_sitterpayment.save()
            return render(request, "sitterpayments/addi.html", {
                "form": SitterPaymentForm(),
                "success": True
            })
    else:
        form = SitterPaymentForm()

    return render(request, "sitterpayments/addi.html", {
        "form": form
    })

def edita(request, id):
    if request.method == "POST":
        sitterpayment = SitterPayment.objects.get(pk=id)
        form = SitterPaymentForm(request.POST, instance=sitterpayment)
        if form.is_valid():
            form.save()
            return render(request, "sitterpayments/edita.html", {
                "form": form,
                "success": True
            })
    else:
        sitterpayment = SitterPayment.objects.get(pk=id)
        form = SitterPaymentForm(instance=sitterpayment)
    return render(request, "sitterpayments/edita.html", {
            "form": form
        })

def delee(request, id):
    if request.method == "POST":
        sitterpayment = SitterPayment.objects.get(pk=id)
        sitterpayment.delete()
    return HttpResponseRedirect(reverse("sitterpayment"))

def logout_view(request):
    logout(request)
    return render(request, "logged_out.html")
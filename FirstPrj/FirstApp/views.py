"""Views module for FirstApp handling customer transactions and searches."""

from django.http import HttpResponse
from django.shortcuts import render
from .forms import CustomerForm, CustomerSearchForm
from .models import Customer


def add_customer(request):
    """View to handle creating a new customer via POST request."""
    if request.method == "POST":
        form = CustomerForm(request.POST)
        if form.is_valid():
            Customer.objects.create(
                first_name=form.cleaned_data["first_name"],
                last_name=form.cleaned_data["last_name"],
                email=form.cleaned_data["email"],
                address_id=form.cleaned_data["address_id"],
                store_id=form.cleaned_data["store_id"],
            )
            return HttpResponse("Customer created successfully!")
    else:
        form = CustomerForm()

    return render(request, "FirstApp/add_customer.html", {"form": form})


def search_customers(request):
    """View to handle searching customers via GET request."""
    form = CustomerSearchForm(request.GET)
    customers = []

    if form.is_valid() and form.cleaned_data.get("search_query"):
        query = form.cleaned_data["search_query"]
        customers = Customer.objects.filter(first_name__icontains=query)
    else:
        customers = Customer.objects.all()[:10]

    return render(
        request,
        "FirstApp/search_customers.html",
        {"form": form, "customers": customers},
    )

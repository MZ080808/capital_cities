from django.shortcuts import render
from django.views.generic import ListView
from django.views.generic.edit import CreateView
from .models import Capital

# Create your views here.


class HomePageView(ListView):
    template_name = "home.html"
    model = Capital


class NewCapitalView(CreateView):
    template_name = "capital_new.html"
    model = Capital
    fields = "__all__"

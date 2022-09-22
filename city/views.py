from django.shortcuts import render
from django.http import HttpResponse


# Create your views here.
def index(request):
    return HttpResponse("<h4>start page</h4>")


def show_city(request):
    pass

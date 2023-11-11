from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def home(request):
    return render(request, 'weekly_plan/home.html')

def weekly_plan(request):
    return render(request, 'weekly_plan/weekly_plan.html')
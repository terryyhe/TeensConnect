from django.shortcuts import render
from django.http import HttpResponse
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from django.contrib import messages

def home(request):
    #messages.add_message(request, messages.INFO, 'Hello world.')
    return render(request, 'home.html', {})

def about(request):
    return render(request, 'about.html', {})

def events(request):
    now = datetime.now()
    cal = HTMLCalendar().formatmonth(
        now.year,
        now.month
    )
    #return render(request, 'events.html', {})
    return render(request, 'events.html', {'cal':cal})

def other(request, year=2022, month="May"):
    month_number = int(list(calendar.month_name).index(month))
    now = datetime.now()
    current_year = now.year
    cal = HTMLCalendar().formatmonth(
        year,
        month_number
    )
    return render(request, 'other.html',\
        {"year": year, "month": month, \
        "month_number": month_number, \
        "current_year": current_year, \
        "now": now.strftime('%I:%M:%S %p'), \
        'cal': cal})

def login_user(request):
    return render(request, 'login.html', {})
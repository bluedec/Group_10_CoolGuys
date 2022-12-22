from django.shortcuts import render, redirect, get_object_or_404
import calendar
from calendar import HTMLCalendar
from django.views.generic import TemplateView
from django.views import generic
from datetime import datetime as dt, timedelta, date
from .models import Event, EventCategory
from django.http import HttpResponse
from .forms import EventForm
import json
from django.utils.safestring import mark_safe
from collections import defaultdict

# Create your views here.

def events(request, year=dt.now().year, month=dt.now().strftime('%B'), day=dt.now().strftime('%d')):
    month = str(month).capitalize()
   
    #convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)
   
    #create a calendar
    cal = HTMLCalendar().formatmonth(
        year, 
        month_number,
        )
    #get current year
    now = dt.now()
    current_year = now.year

    #Query the Events Model for Dates
    event_list = Event.objects.filter(
        event_date__year = year,
        event_date__month = month_number,
    )

    event_days = defaultdict(list)
    for event in event_list:
        event_days[event.event_date.day].append(event)

    # Prev/Next month
    prev_year = int(year)
    next_year = int(year)
    prev_month = int(month_number) - 1
    next_month = int(month_number) + 1
    if prev_month == 0:
        prev_year -= 1
        prev_month = 12
    if next_month == 13:
        next_year += 1
        next_month = 1

    months ={
        1:'January',
        2:'February',
        3:'March',
        4:'April',
        5:'May',
        6:'June',
        7:'July',
        8:'August',
        9:'September',
        10:'October',
        11:'November',
        12:'December',
    }
    if prev_month > 12 or prev_month < 1:
        return render(request, '404.html')
    if next_month > 12 or next_month < 1:
        return render(request, '404.html')

    #get current time
    time = now.strftime('%I:%M %p')
    print(prev_month)
    print(next_month)
    
    return render(request, 
        'cal.html',{
            "year": year,
            "month": month,
            "day": day,
            "month_number": month_number,
            "cal":cal,
            "current_year":current_year,
            "time":time,
            "event_list": event_list,
            "event_days": event_days,
            "prev_month": months[prev_month],
            "next_month": months[next_month],
            "prev_year": prev_year,
            "next_year": next_year,
            
            
        },
        
        )


def all_events(request):
    event_list = Event.objects.all()
    return render(request, 'event_list.html', {
        'event_list': event_list
    })


def event_category(request, eventcategory_id):
    #try:
        event_category = get_object_or_404(EventCategory, id=eventcategory_id)
        events = Event.objects.filter(event_category=eventcategory_id)
        return render(request, 'event_category.html', {
            'event_category':event_category, 
            'events':events,
            })
    #except:
    #    return render(request, '404.html')


    
from django.shortcuts import render, redirect, get_object_or_404
import calendar
from calendar import HTMLCalendar
from datetime import datetime
from .models import Event, EventCategory

# Create your views here.

def events(request, year=datetime.now(), month=datetime.now()):
    month = month.capitalize()
    #convert month from name to number
    month_number = list(calendar.month_name).index(month)
    month_number = int(month_number)

    #create a calendar

    cal = HTMLCalendar().formatmonth(
        year, 
        month_number
        )
    #get current year
    now = datetime.now()
    current_year = now.year

    #get current time
    time = now.strftime('%I:%M %p')

    return render(request, 
        'events.html', {
            "year": year,
            "month": month,
            "month_number": month_number,
            "cal":cal,
            "current_year":current_year,
            "time":time,
        })


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

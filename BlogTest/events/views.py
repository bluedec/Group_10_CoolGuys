from django.shortcuts import render, redirect, get_object_or_404
import calendar
from calendar import HTMLCalendar
from datetime import datetime as dt, timedelta, date
from .models import Event, EventCategory
from django.http import HttpResponse
import json

# Create your views here.

def events(request, year=dt.now().year, month=dt.now().strftime('%B')):
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
        event_date__month = month_number
    
    )

    all_events = Event.objects.all()
    get_event_types = Event.objects.only('event_type')

    if request.GET:
        event_arr = []
        if request.GET.get('event_type') == "all":
            all_events = Event.objects.all()
        else:
            all_events = Event.objects.filter(event_type__icontains=request.GET.get('event_type'))

        for i in all_events:
            event_sub_arr = {}
            event_sub_arr['title'] = i.name
            start_date = dt.strptime(str(i.event_date.date()), "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
            end_date = dt.strptime(str(i.end_date.date()), "%Y-%m-%dT%H:%M:%S").strftime("%Y-%m-%dT%H:%M:%S")
            event_sub_arr['start'] = start_date
            event_sub_arr['end'] = end_date
            event_arr.append(event_sub_arr)
        return HttpResponse(json.dumps(event_arr))

    context = {
        "events": all_events,
        "get_event_types": get_event_types,

    }


    #get current time
    time = now.strftime('%I:%M %p')

    return render(request, 
        'cal.html',{
            "year": year,
            "month": month,
            "month_number": month_number,
            "cal":cal,
            "current_year":current_year,
            "time":time,
            "event_list": event_list,
            
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


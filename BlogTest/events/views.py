from django.shortcuts import render
import calendar
from calendar import HTMLCalendar
from datetime import datetime

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

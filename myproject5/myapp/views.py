import datetime
from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def home(request):
    data = {
        "name":"Jagadish Chakma",
        "email":"jagadishchakma401@gmail.com",
        "phone":"01608355518",
        "city":"rangamati",
        "village":"Bodhipur",
        "friends":["Namita Chakma","Jagadish Chakma","Jotis Moni Chakma","Kajola Chakma","Arnob Chakma"],
        "details":{
            "language":"Python",
            "secondlanguage":"Javascript",
            "country":"Bangladesh",
            "study":"CSE"
        },
        "age":14,
        "fullname":["Jagadish", "Chakma"],
        "date":datetime.datetime.now
    }
    return render(request, 'home.html',data)
def about(request):
    return render(request, 'about.html')
def contact(request):
    return render(request, 'contact.html')
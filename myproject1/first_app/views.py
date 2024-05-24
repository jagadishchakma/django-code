from django.shortcuts import render

# Create your views here.

def home(request):
    data = {
        "fname": "Jagadish",
        "lname": "Chakma",
        "age": 29,
        "study": "BBA",
        "info": [
            {
                "name": "jagadish chakma",
                "age": 29,
                "study": "BBA",
            },
            {
                "name": "namita chakma",
                "age": 30,
                "study": "cse",
            },
            {
                "name": "kajola chakma",
                "age": 40,
                "study": "bbs",
            }
        ]
    }
    return render(request,'home.html', data)
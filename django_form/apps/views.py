from django.shortcuts import render
from . forms import contactForm

# Create your views here.

def home(request):
    return render(request,'home.html')

def about(request):
    return render(request,'about.html')

def contact(request):
    return render(request,'contact.html')

def service(request):
    return render(request,'service.html')

def login(request):
    return render(request,'login.html')

def registration(request):
    return render(request,'registration.html')

def django_form(request):
    if request.method == 'POST':
        form = contactForm(request.POST, request.FILES)
        if form.is_valid():
            file = form.cleaned_data['file']
            with open('./apps/upload/' + file.name, 'wb+') as destination:
                for chunk in file.chunks():
                    destination.write(chunk)
            print(form.cleaned_data)
            # print(file)
            return render(request,'djangoform.html', {'form': form})
    else:
        form = contactForm()
        return render(request,'djangoform.html', {'form': form})
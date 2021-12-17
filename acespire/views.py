from django.shortcuts import render

def home(request) :
    return render(request, 'acespire/home.html')

def products(request) :
    return render(request, 'acespire/products.html')

def whyweare(request) :
    return render(request, 'acespire/whyweare.html')

def research(request) :
    return render(request, 'acespire/research.html')

def about(request) :
    return render(request, 'acespire/about.html')

def career(request) :
    return render(request, 'acespire/career.html')

def contact(request) :
    return render(request, 'acespire/contact.html')

def employee(request) :
    return render(request, 'acespire/employee.html')
from django.http import request
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    return render(request, 'home.html')


def new_user(request):
    if request.method == "POST":
        first_name = request.POST['first_name'],
        last_name = request.POST['last_name'],
        email = request.POST['email'],
        password = request.POST['password'],
        return redirect('/account')
    return render (request, 'new_user.html')


def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
    return render(request, 'login.html')


def order(request):
    if request.method == "POST":
        supreme = request.POST['supreme_pizza'],
        pepperoni = request.POST['pepperoni_pizza'],
        sausage = request.POST['saus_pizza'],
        hawaiian = request.POST['hawaiian_pizza']


        
    return render(request, 'order.html')


def checkout(request):
    return render(request, 'checkout.html')


def account(request):
    if request.method == "POST":
        request.session['first_name'] = request.POST['first_name'],
        request.session['last_name'] = request.POST['last_name'],
        request.session['email'] = request.POST['email'],
        request.session['password'] = request.POST['password'],
    return render(request, 'account.html')


def edit(request, id):
    edit_user = User.objects.get(id=id)
    edit_user.first_name = request.session['first_name']
    edit_user.last_name = request.session['last_name']
    edit_user.email = request.session['email']
    edit_user.save()
    return redirect('/account')


def delete(request, id):
    delete_pizza = Pizza.objects.get(id=id)
    delete_pizza.delete()
    return redirect('/checkout')
    

def logout(request):
    request.session.flush()
    return redirect('/')

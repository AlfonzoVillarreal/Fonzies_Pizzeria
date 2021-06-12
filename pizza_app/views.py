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
    
    return render(request, 'order.html')

def checkout(request):
    return render(request, 'checkout.html')

def account(request):
    if request.method == "POST":
        request.session['first_name'] = request.POST['first_name'],
        request.session['last_name'] = request.POST['last_name'],
        request.session['email'] = request.POST['email'],
        request.session['password'] = request.POST['password'],
    return redirect('/account.html',)

def logout(request):
    request.session.flush()
    return redirect('/')

def edit(request, id):
    edit_user = User.objects.get(id=id)

    edit_user.first_name = request.POST['first_name']
    edit_user.last_name = request.POST['last_name']
    edit_user.email = request.POST['email']
    edit_user.save()

    order_edit = Order.objects.get(id=id)
    order_edit.quantity_ordered = request.POST['quan']
    order_edit.total_price = request.POST['']
    order_edit.save()

    pizza_edit = Pizza.objects.get(id=id)
    pizza_edit.descriptions = request.POST['']
    pizza_edit.price = request.POST['']
    pizza_edit.save()
    return redirect('/account')

def delete(request, id):
    delete_pizza = Pizza.objects.get(id=id)
    delete_pizza.delete()
    return redirect('/checkout')
from django.http import request
from django.shortcuts import render, redirect
from .models import *


# Create your views here.
def home(request):
    request.session.flush()
    return render(request, 'home.html')

def new_user(request):
    if request.method == "POST":
        errors = User.objects.reg_validator(request.POST)
        print(errors)


    new_user = User.objects.create(
        first_name = request.POST['fname'], 
        last_name = request.POST['lname'], 
        email = request.POST['email'], 
        password = request.POST['password']
    )
    request.session['user'] = new_user.first_name
    request.session['id'] = new_user.id
    return redirect ('/')

def login(request):
    if request.method == "POST":
        errors = User.objects.login_validator(request.POST)
        return redirect('/')

    
    return render(request, 'login.html')

def order(request):
    return render(request, 'order.html')

def checkout(request):
    return render(request, 'checkout.html')

def account(request):
    context = {
        'user': User.objects.get(id=id)
    }
    return render(request, 'account.html', context)

def logout(request):
    request.session.flush()
    return redirect('/')

def edit(request, id):
    edit_user = User.objects.get(id=id)

    edit_user.first_name = request.POST['fname']
    edit_user.last_name = request.POST['lname']
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
    destroy = Pizza.objects.get(id=id)
    destroy.delete()
    return redirect('/order')
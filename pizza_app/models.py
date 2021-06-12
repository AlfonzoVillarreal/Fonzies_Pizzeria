from django.db import models
import re

class UserManager(models.Manager):
    def reg_validator(self, postData):
        errors = {}
        if len(postData['first_name']) < 2:
            errors['first_name'] = "First Name must be at least 2 characters long."
        if len(postData['last_name']) < 2:
            errors['last_name'] = "Last Name must be at least 2 characters long."
        email_regex = re.compile(
            r'^[a-zA-Z0-9.+_-]+@[a-zA-Z0-9._-]+\.[a-zA-Z]+$')
        if len(postData['email']) == 0:
            errors['email'] = "You must enter an email."
        elif not email_regex.match(postData['email']):
            errors['email'] = "Must be a valid email."
        current_users = User.objects.filter(email = postData['email'])
        if len(current_users) > 0:
            errors['duplicate'] = "That email is already in use."
        if len(postData['password']) < 8:
            errors['password'] = "Password must be at least 8 characters long."
        return errors


    def login_validator(self, postData):
        errors = {}
        existing_user = User.objects.filter(email=postData['email'])

        if len(existing_user) != 1:
            errors['email'] = "User does not exist."
        if len(postData['email']) == 0:
            errors['email'] = "Email must be entered."
        if len(postData['password']) < 8:
            errors['password'] = "An eight character password must be entered."           
        return errors


#User
class User(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    objects = UserManager()
    #user orders

#Order
class Order(models.Model):
    quantity_ordered = models.IntegerField()
    total_price = models.DecimalField(decimal_places=2, max_digits=6)
    orders = models.ForeignKey(User, related_name='user_orders', on_delete=models.CASCADE)
    #pizza orders

#Pizza
class Pizza(models.Model):
    name = models.CharField(max_length=45)
    description = models.CharField(max_length=255)
    price = models.DecimalField(decimal_places=2, max_digits=5)
    pizzas = models.ForeignKey(Order, related_name='pizza_orders', on_delete=models.CASCADE)
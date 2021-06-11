from django.urls import path
from . import views

urlpatterns = [
    path('', views.home),
    path('new_user', views.new_user),
    path('login', views.login),
    path('order', views.order),
    path('checkout', views.checkout),
    path('account', views.account),
    path('logout', views.logout),
    path('<int:id>/edit', views.edit),
    path('<int:id>/delete', views.delete),
]
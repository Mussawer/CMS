from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Order, Customer


class OrderForm(ModelForm):
    #this meta class represents which model to use and all of its fields to use in Form
    class Meta:
        model = Order
        fields = '__all__'


class CreateUserForm(UserCreationForm):
    #this meta class represents which model to use and which of field to use in Form
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class CustomerForm(ModelForm):
    #this meta class represents which model to use and all of its field to use except user Form
    class Meta:
        model = Customer
        fields = '__all__'
        exclude = ['user']

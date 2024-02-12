from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


from .models import *

class ItemForm(ModelForm):
    class Meta:
        model = Item
        fields = ['name', 'sku', 'category', 'tags', 'stock_status', 'available_stock']


# class CustomerForm(ModelForm):
#     class Meta:
#         model = Customer
#         fields = '__all__'
#         exclude = ['user']


class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username','email', 'password1', 'password2']
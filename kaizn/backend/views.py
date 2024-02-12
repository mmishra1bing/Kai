from django.shortcuts import render, redirect
from .forms import *
from django.forms import inlineformset_factory
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .models import *
# from .filters import OrderFilter
from django.http import JsonResponse
from django.db.models import Q

# Create your views here.


def is_valid_queryparam(param):
    return param != '' and param is not None



# LOGIN AND USER REGISTRATION VIEWS
def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, "Account was created for " + username)
            return redirect('login')

    context = {
        'form': form,
    }
    return render(request, 'backend/register.html', context)


def loginPage(request):
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        # Check if username or password is empty
        if not username or not password:
            messages.error(request, "Username and password are required!")
            return render(request, 'backend/login.html', {})

        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('products')
        
        else:
            messages.info(request, "Username OR Password is incorrect!")

    context = {}
    return render(request, 'backend/login.html', context)


def logoutUser(request):
    logout(request)
    return redirect('login')


# DashBoard VIEW# # DASHBOARD VIEW
# @login_required(login_url='login')
def products(request):
    items = Item.objects.all()

    # Search
    search_query = request.GET.get('search_query')
    if search_query:
        items = items.filter(
            Q(name__icontains=search_query) |
            Q(sku__icontains=search_query) |
            Q(category__icontains=search_query) |
            Q(tags__icontains=search_query)
        )

    # Filter
    category_filter = request.GET.get('category')
    if category_filter:
        items = items.filter(category=category_filter)

    # Filter by stock status
    stock_status_filter = request.GET.get('stock_status')
    if stock_status_filter:
        items = items.filter(stock_status__lte=stock_status_filter)

    stock_status_filter = request.GET.get('stock_status')
    if stock_status_filter:
        items = items.filter(stock_status=stock_status_filter)

    # Sort
    sort_by = request.GET.get('sort_by')
    if sort_by:
        items = items.order_by(sort_by)

    serialized_items = [{'name': item.name,
                         'sku': item.sku,
                         'category': item.category,
                         'tags': item.tags,
                         'stock_status': item.stock_status,
                         'available_stock': item.available_stock} for item in items]

    return JsonResponse({'items': serialized_items})

# @login_required(login_url='login')
# def products(request):
#     products = Item.objects.all().order_by('name')
#     # items = Item.objects.all()
#     # print(request)
#     # total_products = products.all()
#     context = {
#         'products': products,
#         # 'total_products': total_products,
#     }
#     return render(request, 'backend/product.html', context)


@login_required(login_url='login')
def CreateProduct(request):
    form = ItemForm()
    if request.method == "POST":
        form = ItemForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {
        'form': form,
    }
    return render(request, 'backend/create_product.html', context)


@login_required(login_url='login')
def UpdateProduct(request, pk):
    product = Item.objects.get(id=pk)
    form = ItemForm(instance=product)
    if request.method == 'POST':
        form = ItemForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('products')
    context = {
        'form': form,
    }
    return render(request, 'backend/update_product.html', context)

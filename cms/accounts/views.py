from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import *
from .forms import OrderForm

# Create your views here.

def home(request):
    #getting all orders to show on dashboard
    orders = Order.objects.all()
    
    #getting all customers
    customers = Customer.objects.all()
    
    #counting all orders
    total_orders = orders.count()
    #counting all customers
    total_customers = customers.count()
    #counting delivered orders
    delivered = orders.filter(status='Delivered').count()
    #totala pending orders
    pending = orders.filter(status='Pending').count()
    
    context = { 'orders': orders, 'customer':customers,
               'total_orders': total_orders, 'delivered': delivered,
               'pending': pending}
    
    #returning data to be displayed in the template
    return render(request, 'accounts/dashboard.html', context)
    
def products(request):
    products = Product.objects.all()
    return HttpResponse(request, 'accounts/products.html', {'products':products})

def customer(request, pk):
    customers = Customer.objects.get(id=pk)
    
    #Returns all child models related to parent
    orders = customer.order_set.all()
    order_count = orders.count()
    
    context = {'customer':customer, 'orders':orders, 'order_count':order_count}
    return HttpResponse(request, 'accounts/customer.html', context) 

def createOrder(request):
    form = OrderForm()
    if request.method == 'POST':
        form = OrderForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/')
    context = {'form': form}
    return render(request, 'accounts/order_form.html', context)

def updateOrder(request, pk):
    
    order = Order.objects.get(id=pk)
    form = OrderForm(instance=order)
    
    if request.method == 'POST':
        form = OrderForm(request.POST, instance=order)
        if form.is_valid():
            form.save()
            return redirect('/')
    
    context = {'item': order}
    return render(request, 'accounts/order_form.html', context)

def deleteOrder(request, pk):
    order = Order.objects.get(id=pk)
    if request.method == 'POST':
        order.delete()
        return redirect('/')
    
    context = {'item': order}
    return render(request, 'accounts/delete.html', context)
    

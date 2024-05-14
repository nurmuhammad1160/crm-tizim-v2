from django.shortcuts import render, redirect
from .forms import LoginForm, EditProductForm, createForm, CreateUserProfil
from .models import Product, UserProfile, Income
from django.contrib.auth import login, authenticate, logout
from django.http import JsonResponse
from django.contrib.auth.models import User
from django.views.decorators.cache import cache_page
from django.core import serializers
from django.views.decorators.csrf import csrf_exempt
from django.utils import timezone
import json

def barcha(request, cat):
    products = Product.objects.filter(category=cat)
    for product in products:
        product.summa_result = product.amount * product.summa
        product.dollor_result = product.amount * product.dollor
    return render(request, 'boshliq/barcha.html', {'product': products})

def deleteProduct(request, p_id):
    product = Product.objects.get(pk=p_id)
    product.delete()
    return redirect('barcha')

def editProduct(request, p_id):
    product = Product.objects.get(pk=p_id)
    form =EditProductForm(request.POST or None)
    if request.method == 'POST':
        form = EditProductForm(request.POST, instance=product)
        if form.is_valid():
            form.save()
            return redirect('barcha')

    else:
        form = EditProductForm(instance=product)
        
    return render(request, 'boshliq/editProduct.html', {'product':product,'form':form})

def createProduct(request):
    form = createForm(request.POST or None)
    if request.method == 'POST':
        if form.is_valid():
            form.save()
            return redirect('barcha')
        
    return render(request, 'boshliq/create.html',{'form':form})

def detailProduct(request, p_id):
    product = Product.objects.get(pk=p_id)
    product.summa_result = product.amount * product.summa
    product.dollor_result = product.amount * product.dollor
    return render(request, 'boshliq/view.html',{'product':product})

def login_user(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        for product in products:
            product.summa_result = product.amount * product.summa
            product.dollor_result = product.amount * product.dollor
        return render(request, 'boshliq/barcha.html', {'product': products})
    else:
        if request.method == 'POST':
            username = request.POST['username']
            password = request.POST['password']
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('home')
        if request.method == 'GET':  
            return render(request, 'login.html')

def home(request):
    if request.user.is_authenticated:
        products = Product.objects.all()
        for product in products:
            product.summa_result = product.amount * product.summa
            product.dollor_result = product.amount * product.dollor
        return render(request, 'boshliq/barcha.html', {'product': products})

    else:
        return redirect('login')
        
    form = LoginForm()
        # return render(request, 'login.html', {'form': form})
    
    if request.method == 'POST':
        form = LoginForm(request.POST)
        
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(request,username=username,password=password)
            if user:
                login(request, user)
                print('login amalga oshirildi')
                return redirect('home')
            else:
                print('xato')
       
    return render(request,'login.html',{'form': form})
    
def sign_out(request):
    logout(request)
    return redirect('login')   

def productSearch(request):
    q = request.GET.get('q')
    if q:
        query = Product.objects.filter(name__icontains=q)
        query = [{'name': product.name, 'type':product.type, 'id': product.id, 'amount': product.amount, 'summa': product.summa, 'dollor': product.dollor, 'sum': product.amount*product.summa, 'valuta': product.amount*product.dollor} for product in query]
    else:
        query = None
    return JsonResponse(data=query, safe=False)

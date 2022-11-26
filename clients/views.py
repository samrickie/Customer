import parameters as parameters
from django.contrib import auth
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import DetailView, ListView

from .models import Userz, Collector, Post


# Create your views here.
# registration form


def userdata(request):
    if request.method == 'POST':
        first_name = request.POST['firstname']
        last_name = request.POST['lastname']
        phone = request.POST['phone']
        email = request.POST['email']
        location = request.POST['location']
        gender = request.POST['gender']
        username = request.POST['username']
        password = request.POST['password']

        new_user = User(username=username, password=password, first_name=first_name, last_name=last_name, email=email,
                        is_staff=True, is_active=True)
        new_user.save()
    return render(request, 'register.html')


# collector form

def collector(request):
    if request.method == 'POST':
        product_name = request.POST.get('product_name', False)
        quantity = request.POST.get('quantity', False)
        price = request.POST.get('price', False)
        place = request.POST.get('place', False)
        brand_name = request.POST.get('brand_name')
        product_image = request.POST.get('product_img', False)
        receipt_image = request.POST.get('product_receipt', False)

        new_product = Collector(product_name=product_name, quantity=quantity, price=price, place=place,
                                brand_name=brand_name,
                                product_image=product_image, Receipt_image=receipt_image)
        new_product.save()

    return render(request, 'collector.html')


class UserDetailsView(ListView):
    model = Collector
    template_name = 'repoort.html'


def login_view(request):
    if request.POST:
        _username = request.POST['uname']
        _password = request.POST['pwd']

        user = auth.authenticate(request, username=_username, password=_password)

        if user:
            auth.login(request, user)
            return redirect('collector')
        else:
            return redirect('_login')

    else:

        return render(request, 'login.html')


def logout_view(request):
    logout(request)
    redirect('_login')


class Post(ListView):
    model = Post
    template_name = 'home.html'

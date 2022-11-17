from django.shortcuts import render
from django.views.generic import DetailView

from clients.models import User, Collector


# Create your views here.
# registration form
def register(request):
    if request.method == 'POST':
        first_name = request.POST['']
        last_name = request.POST['']
        phone = request.POST['']
        email = request.POST['']
        location = request.POST['']
        gender = request.POST['']
        username = request.POST['']
        pasword = request.POST['']

        new_user = User(first_name=first_name, last_name=last_name, phone=phone, email=email,
                        location=location, gender=gender, username=username, pasword=pasword)
        new_user.save()
    return render(request, "registration-page.html")


# collector form

def collector(request):
    if request.method == 'POST':
        product_name = request.POST['']
        quantity = request.POST['']
        price = request.POST['']
        place = request.POST['']
        brand_name = request.POST['']
        product_image = request.POST['']
        receipt_image = request.POST['']

        new_product = Collector(product_name=product_name, quantity=quantity, price=price, place=place,
                                brand_name=brand_name,
                                product_image=product_image, receipt_image=receipt_image)
        new_product.save()

    return render(request, 'collector.html')


class CustomerDetailsView(DetailView):
    model = User, Collector
    template_name = 'customer/report.html'

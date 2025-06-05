from django.http import JsonResponse, HttpResponse
from django.shortcuts import render, get_object_or_404
from django.template import loader
from .models import User, Product, Cart, CartItem

def home(request):
    product_list = []
    for obj in Product.objects.all():
        product_list.append(obj)
    template = loader.get_template("heavenlyvitamin/index.html")
    context = {"Product list": product_list}
    return HttpResponse(template.render(context, request))

def display_username(request, username):
    user = get_object_or_404(User, username=username)
   
    response = {
        "username" : user.username,
        "first_name": user.first_name,
        "last_name": user.last_name,
        "email": user.email,
        "phone_number": user.phone_number,
        "birthdate": user.birthdate,
    }
    return JsonResponse(response) 

def display_product(request, id):
    product = get_object_or_404(Product, id=id)

    response = {
        "product_name": product.product_name,
        "price": product.price,
        "brand": product.brand,
        "description": product.description,
    }
    return JsonResponse(response)

def display_cart(request, username):
    user = get_object_or_404(User, username=username)
    cart = get_object_or_404(Cart, user = user)

    response = {
        "username" : cart.user.username,
        "cart_isactive" : cart.is_active,
        "total_price" : cart.total_price,
        "total_items": cart.total_items,
    }

    return JsonResponse(response)

# def validate_account(request, username):
#     user = get_object_or_404(User, username=username)

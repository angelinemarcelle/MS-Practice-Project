from django.urls import path

from . import views

app_name = "heavenlyvitamin"

urlpatterns = [
    path("", views.home, name="index"),
    path("user/<str:username>/", views.display_username, name="username"),
    path("user/<str:username>/cart", views.display_cart, name="username"),
    path("product/id=<str:id>/", views.display_product, name="id"),
    path("account/<str:username>", views.display_username, name="username"),
]
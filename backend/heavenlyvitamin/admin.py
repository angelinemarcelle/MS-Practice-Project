from django.contrib import admin
from .models import User, Product, Cart, CartItem

# Register your models here.

@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'first_name', 'last_name', 'email', 'phone_number', 'birthdate']
    search_fields = ['id','username', 'email', 'first_name', 'last_name']
    list_filter = ['birthdate']
    ordering = ['id']

@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id','product_name', 'description', 'brand', 'price', 'stock', 'status', 'category', 'count', 'product_image']
    search_fields = ['id','product_name', 'brand', 'description']
    list_filter = ['status', 'category', 'count']
    ordering = ['id']

class CartItemInline(admin.TabularInline):
    model = CartItem
    extra = 1
    fields = ['product', 'quantity', 'subtotal']
    readonly_fields = ['subtotal']

@admin.register(Cart)
class cartAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_username', 'is_active', 'total_price', 'total_items']
    list_filter = ['is_active', 'user__username']
    search_fields = ['user__username']
    ordering = ['user__username']
    inlines = [CartItemInline]

    def get_username(self, obj):
        return obj.user.username
    get_username.admin_order_field = 'user__username'  # Allows sorting
    get_username.short_description = 'Username'  # Column header

@admin.register(CartItem)
class cartItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'get_username', 'product', 'quantity', 'subtotal']
    list_filter = ['cart__user__username', 'product']
    search_fields = ['cart__user__username', 'product__product_name']

    def get_username(self, obj):
        return obj.cart.user.username
    get_username.admin_order_field = 'cart__user__username'
    get_username.short_description = 'Username'



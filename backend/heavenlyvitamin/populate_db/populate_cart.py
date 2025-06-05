import os
import sys
import django
import random

# Setup Django environment
sys.path.append("/Users/angelinemarcellelukito/MS Project Learn/backend")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from heavenlyvitamin.models import User, Product, Cart, CartItem

def populate_carts():
    users = User.objects.all()
    products = list(Product.objects.all()) 

    if not users:
        print("No users found. Please populate users first.")
        return

    if not products:
        print("No products found. Please populate products first.")
        return

    # Create carts for each user
    for user in users:
        try:
            # Create a cart for the user
            cart = Cart.objects.create(
                user=user,
                is_active=True
            )

            # Randomly select 1-3 products for this cart
            num_products = random.randint(1, 3)
            selected_products = random.sample(products, num_products)

            # Add products to cart
            for product in selected_products:
                quantity = random.randint(1, 5)  # Random quantity between 1 and 5
                CartItem.objects.create(
                    cart=cart,
                    product=product,
                    quantity=quantity
                )
            
            # Print cart details
            print(f"\nCreated cart for {user.username}:")
            cart_items = CartItem.objects.filter(cart=cart)
            for item in cart_items:
                print(f"- {item.product.product_name} (Qty: {item.quantity}, Subtotal: Rp{item.subtotal:,})")
            print(f"Total Items: {cart.total_items}")
            print(f"Total Price: Rp{cart.total_price:,}")

        except Exception as e:
            print(f"Error creating cart for user {user.username}: {str(e)}")

if __name__ == '__main__':
    print("Starting cart population...")
    print("\nCreating random carts...")
    populate_carts()

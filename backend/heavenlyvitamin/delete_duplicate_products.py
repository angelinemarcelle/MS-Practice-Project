import os
import sys
import django

# Setup Django environment
sys.path.append("/Users/angelinemarcellelukito/MS Project Learn/backend")
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from heavenlyvitamin.models import Product
from django.db.models import Count

def delete_duplicate_products():
    duplicates = Product.objects.values('product_name').annotate(
        name_count=Count('product_name')
    ).filter(name_count__gt=1)
    for dup in duplicates:
        product_name = dup['product_name']
        # Keep the first one, delete the rest
        products = Product.objects.filter(product_name=product_name).order_by('id')
        # Keep the first one
        first_product = products.first()
        # Delete the rest
        products.exclude(id=first_product.id).delete()
        print(f"Kept ID:{first_product.id} for {product_name} and deleted the duplicates")

if __name__ == '__main__':
    print("Starting duplicate removal...")
    delete_duplicate_products()
    print("Duplicate removal complete!")

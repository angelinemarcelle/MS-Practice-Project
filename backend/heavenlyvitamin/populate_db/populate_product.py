import os
import sys
import django

# Add the current directory to Python path
sys.path.append("/Users/angelinemarcellelukito/MS Project Learn/backend")

# Setup Django
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'mysite.settings')
django.setup()

from heavenlyvitamin.models import Product
from datetime import date

def populate_products():
    products_data = [
    {
        "product_name": "UpNourish N.O. Nitric Oxide Booster Mixed Berry",
        "description": "Pre-workout nitric oxide booster with mixed berry flavor for enhanced performance and muscle pump",
        "brand": "UpNourish",
        "price": 600000,
        "stock": 50,
        "product_image": {"url": "upnourish_no.jpg"},
        "status": Product.Status.IN_STOCK,
        "category": Product.Category.SUPPLEMENTS,
        "count": 30
    },
    {
        "product_name": "Micro Ingredients Liver Detox",
        "description": "20-in-1 liver cleanse and repair supplement with natural ingredients",
        "brand": "Micro Ingredients",
        "price": 700000,
        "stock": 75,
        "product_image": {"url": "liver_detox.jpg"},
        "status": Product.Status.IN_STOCK,
        "category": Product.Category.SUPPLEMENTS,
        "count": Product.Count.TWO_FORTY
    },
    {
        "product_name": "Micro Ingredients Pure Methylated B Complex",
        "description": "Advanced B-Complex vitamin supplement with enhanced methylation",
        "brand": "Micro Ingredients",
        "price": 900000,
        "stock": 100,
        "product_image": {"url": "methyl_b.jpg"},
        "status": Product.Status.IN_STOCK,
        "category": Product.Category.VITAMINS,
        "count": Product.Count.TWO_FORTY
    },
    {
        "product_name": "Micro Ingredients Niacin",
        "description": "Vitamin B3 500mg supplement for energy metabolism and cardiovascular health",
        "brand": "Micro Ingredients",
        "price": 650000,
        "stock": 60,
        "product_image": {"url": "niacin.jpg"},
        "status": Product.Status.LOW_STOCK,
        "category": Product.Category.VITAMINS,
        "count": Product.Count.THREE_HUNDRED
    },
    {
        "product_name": "Micro Ingredients Moringa",
        "description": "Pure Moringa Oleifera 6,000mg supplement, rich in nutrients and antioxidants",
        "brand": "Micro Ingredients",
        "price": 800000,
        "stock": 85,
        "product_image": {"url": "moringa.jpg"},
        "status": Product.Status.IN_STOCK,
        "category": Product.Category.SUPPLEMENTS,
        "count": Product.Count.THREE_HUNDRED
    },
    {
        "product_name": "PrimeMD LIVER Cleanse & Support",
        "description": "Comprehensive liver support formula with milk thistle and natural ingredients",
        "brand": "PrimeMD",
        "price": 900000,
        "stock": 0,
        "product_image": {"url": "primemd_liver.jpg"},
        "status": Product.Status.OUT_STOCK,
        "category": Product.Category.SUPPLEMENTS,
        "count": 90
    },
    {
        "product_name": "Garden of Life Probiotics Men's Daily",
        "description": "Formulated probiotics specifically designed for men's health",
        "brand": "Garden of Life",
        "price": 1050000,
        "stock": 25,
        "product_image": {"url": "gol_probiotics.jpg"},
        "status": Product.Status.LOW_STOCK,
        "category": Product.Category.SUPPLEMENTS,
        "count": 30
    },
    {
        "product_name": "Sports Research Vitamin K2",
        "description": "Vitamin K2 100mcg with Coconut MCT Oil for enhanced absorption",
        "brand": "Sports Research",
        "price": 1000000,
        "stock": 40,
        "product_image": {"url": "sr_k2.jpg"},
        "status": Product.Status.IN_STOCK,
        "category": Product.Category.VITAMINS,
        "count": Product.Count.ONE_TWENTY
    }
    ]

    for product_data in products_data:
        try:
            product = Product.objects.create(**product_data)
            print(f"Created product: {product.product_name}")
        except Exception as e:
            print(f"Error creating product {product_data['product_name']}: {str(e)}")

if __name__ == '__main__':
    #Product DB
    print("Starting product population script...")
    populate_products()
    print("Product population complete!")



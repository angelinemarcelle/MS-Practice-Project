from django.db import models

# Create your models here.
class User(models.Model):
    username = models.CharField(max_length=30, unique=True)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=30)
    email = models.EmailField(unique=True)
    phone_number = models.CharField(max_length=15, blank=True, null=True)
    birthdate = models.DateField(blank=True, null=True)

    def __str__(self):
        return self.username #Defines the object as username

class Product(models.Model):
    class Status(models.TextChoices):
        IN_STOCK = 'IN', 'In Stock'
        OUT_STOCK = 'OUT', 'Out of Stock'
        LOW_STOCK = 'LOW', 'Low Stock'
        DISCONTINUED = 'DISC', 'Discontinued'

    class Category(models.IntegerChoices):
        VITAMINS = 1, 'Vitamins'
        SUPPLEMENTS = 2, 'Supplements'
        PROTEINS = 3, 'Proteins'
        MEDICINE = 4, 'Medicine'

    class Count(models.IntegerChoices):
        TEN = 10, '10 count'
        THIRTY = 30, '30 count'
        NINETY = 90, '90 count'
        ONE_TWENTY = 120, '120 count'
        ONE_EIGHTY = 180, '180 count'
        TWO_FORTY = 240, '240 count',
        THREE_HUNDRED = 300, '300 count'

    product_name = models.CharField(max_length=100)
    description = models.TextField()
    brand = models.CharField(max_length=50)
    price = models.IntegerField()
    stock = models.IntegerField()
    product_image = models.JSONField() 
    category = models.IntegerField()

    status = models.CharField(
        max_length=4,
        choices=Status.choices,
        default=Status.IN_STOCK
    )
    
    category = models.IntegerField(
        choices=Category.choices,
        default=Category.VITAMINS
    )
    
    count = models.IntegerField(
        choices=Count.choices,
        default=Count.THIRTY
    )

    def __str__(self):
        return self.product_name #Defines the object as product name

class Cart(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    is_active = models.BooleanField(default=True)

    @property
    def total_price(self):
        return sum(item.subtotal for item in self.items.all())
    
    @property
    def total_items(self):
        return sum(item.quantity for item in self.items.all())
    
    def __str__(self):
        return f"{self.user.username}'s Cart" #Defines object as a username's cart

class CartItem(models.Model):
    cart = models.ForeignKey(Cart, related_name='items', on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=1)

    class Meta:
        unique_together = ('cart', 'product') 

    @property
    def subtotal(self):
        return self.product.price * self.quantity

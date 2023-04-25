from django.db import models
# from userprofile.models import Profile
from django.contrib.auth.models import User

# Create your models here.
class Category(models.Model):
    title = models.CharField(max_length=50)
    slug = models.SlugField()
    img = models.ImageField( upload_to='Category', default='category.jpg')
    description = models.TextField()
    
    def _str_(self):
        return self.title
    
    class Meta:
        db_table = 'category'
        managed = True
        verbose_name = 'Category'
        verbose_name_plural = 'Category'
    
class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    name = models.CharField(max_length=50)
    slug = models.SlugField()
    img = models.ImageField(upload_to='product', default='product.jpg')
    price = models.FloatField()
    max_quantity = models.IntegerField()
    min_quantity = models.IntegerField()
    brands = models.CharField(max_length=50, default=50)
    description = models.TextField()
    date_updated = models.DateField(auto_now_add=True)
    date_uploaded = models.DateField(auto_now=True)

    def _str_(self):
        return self.title
    
    class Meta:
        db_table = 'product'
        managed = True
        verbose_name = 'Product'
        verbose_name_plural = 'Product'
    
class Contact(models.Model):
    STATUS_CHOICES = [
        ('New', 'New'),
        ('pending', 'pending'),
        ('completed', 'completed'),
    ]
    firstName = models.CharField(max_length=50)
    lastName = models.CharField(max_length=50)
    subject = models.CharField(max_length=70)
    email = models.EmailField()
    message = models.TextField()
    date_created = models.DateTimeField(auto_now_add=True)
    status = models.CharField(max_length=50, default='New', choices=STATUS_CHOICES)

    def _str_(self):
        return self.firstName 
        
    class Meta:
        db_table = 'contact'
        managed = True
        verbose_name = 'Contact'
        verbose_name_plural = 'Contact'
        
# class signin(models.Model):
#      def _str_(self):
#           return self.firstName
     
class Shopcart(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    quantity = models.IntegerField()
    title = models.CharField(max_length=50)
    order_no = models.CharField(max_length=50)
    amount = models.IntegerField()
    paid = models.BooleanField(default=False)
    price = models.IntegerField()
    date_created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.name
    
    class Meta:
         db_table = 'shopcart'
         managed = True
         verbose_name = 'Shopcart'
         verbose_name_plural = 'Shopcart'
     
class Payment(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.EmailField()
    amount = models.CharField(max_length=50)
    paid = models.BooleanField()
    phone = models.CharField(max_length=50)
    address = models.CharField(max_length=50, default='')
    shop_code = models.CharField(max_length=50)
    pay_code = models.CharField(max_length=50)
    pay_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.user.username
    
    class Meta:
         db_table = 'payment'
         managed = True
         verbose_name = 'Payment'
         verbose_name_plural = 'Payment'
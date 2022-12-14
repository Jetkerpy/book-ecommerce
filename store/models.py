from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse

# Create your models here.


class ProductManager(models.Manager):
    def get_queryset(self):
        return super(ProductManager, self).get_queryset().filter(is_active = True)





class Category(models.Model):
    name = models.CharField(max_length=255, db_index=True)
    slug = models.SlugField(max_length=255, unique=True)



    class Meta:
        verbose_name_plural = 'categories'
    

    def __str__(self):
        return self.name


    
    def get_absolute_url(self):
        return reverse('store:category', kwargs={'category_slug': self.slug})




class Product(models.Model):
    category = models.ForeignKey(Category, related_name='product', on_delete=models.CASCADE)
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name='product_creator')
    title = models.CharField(max_length=255)
    author = models.TextField(max_length=255, default='admin')
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to = 'images/', default = 'images/default.webp')
    slug = models.SlugField(max_length=255)
    price = models.DecimalField(max_digits=4, decimal_places=2)
    in_stock = models.BooleanField(default=True)
    is_active = models.BooleanField(default=True)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager() #default ok
    products = ProductManager()



    class Meta:
        verbose_name_plural = 'Products'
        ordering = ('-created',)

    

    def __str__(self):
        return self.title


    def get_absolute_url(self):
        return reverse('store:detail', kwargs={'slug':self.slug})


    






from django.contrib import admin

from .models import Category, Product

# Register your models here.



@admin.register(Category)

class CategoryAdmin(admin.ModelAdmin):
    list_display = ['name', 'slug']
    prepopulated_fields = {'slug': ('name',)}
    #prepopulated_fields degenimiz bul yagniy men name ne jazsam
    #soni shigaradi slug betde misali name python go desem
    #slug betde python-go dep ozi avtomat tarizde jazadi
    




@admin.register(Product)

class ProductAdmin(admin.ModelAdmin):
    list_display = ['title', 'author', 'slug', 'price', 'in_stock', 'created', 'updated']
    list_filter = ['in_stock', 'is_active']
    list_editable = ['price', 'in_stock']

    prepopulated_fields = {'slug': ('title',)}


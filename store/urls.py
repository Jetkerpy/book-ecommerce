from django.urls import path

from .views import all_products, category_list, product_detail

app_name = 'store'

urlpatterns = [
    path('', all_products, name = 'all-products'),
    path('book/<slug:slug>/', product_detail, name = 'detail'),
    path('category/<slug:category_slug>/', category_list, name = 'category'),
    
    



]
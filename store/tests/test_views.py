from unittest import skip

from django.contrib.auth.models import User
from django.http import HttpRequest
from django.test import Client, RequestFactory, TestCase
from django.urls import reverse

from store.models import Category, Product
from store.views import all_products

# @skip("Demonstrating skipping")
# class TestSkip(TestCase):
#     def test_skip_example(self):
#         pass




class TestViewResponses(TestCase):
    def setUp(self) -> None:
        self.c = Client()
        self.factory = RequestFactory()

        self.cat1 = Category.objects.create(
            name = 'django',
            slug = 'django'
        )

        self.user1 = User.objects.create_user(
            username = 'user',
            email = 'user@a.com',
            password = '12221'
        )

        self.product = Product.objects.create(
            category = self.cat1,
            created_by = self.user1,
            title = 'django new',
            description = 'yeaa',
            slug = 'django-new',
            price = '20.99',
            image = 'django'

        )



    # def test_home_page(self):
    # """
    # Test homepage response status
    
    # """

    def test_url_allowed_hosts(self):
        """
        Test allowed hosts

        """
        response = self.c.get('/', HTTP_HOST = 'nooaddress.co')
        self.assertEqual(response.status_code, 400)

        response = self.c.get('/', HTTP_HOST = 'yourdomain.com')
        self.assertEqual(response.status_code, 200)

        #





    def test_product_detail_url(self):
        response = self.c.get(reverse('store:detail', kwargs={'slug': 'django-new'}))
        
        self.assertEqual(response.status_code, 200)



    def test_category_detail_url(self):
        response = self.c.get(reverse('store:category', kwargs={'category_slug': 'django'}))
        
        self.assertEqual(response.status_code, 200)



    
    def test_homepage_html(self):
        request = HttpRequest()
        response = all_products(request)
        html = response.content.decode('utf8') #bul home htmldi html koriniste qaytaradi
        # print(html)
        self.assertIn('<title>BookStore</title>', html)
        self.assertEqual(response.status_code, 200)



    
    def test_view_function(self):
        request = self.factory.get('book/django-new')
        response = all_products(request)
        self.assertEqual(response.status_code, 200)
        
        











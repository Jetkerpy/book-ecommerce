from django.contrib.auth.models import User
from django.test import TestCase

from store.models import Category, Product


class TestCategoriesModel(TestCase):
    def setUp(self) -> None:
        self.data1 = Category.objects.create(
            name = 'django',
            slug = 'django'
        )


    
    def test_category_model_entry(self):
        data = self.data1
        self.assertTrue(isinstance(data, Category))


    
    def test_category_return_name(self):
        data = str(self.data1)
        self.assertEqual(data, 'django')




class TestProductsModel(TestCase):

    def setUp(self) -> None:
        self.cat1 = Category.objects.create(
            name = 'django',
            slug = 'django'
        )

        self.user1 = User.objects.create_user(
            username = 'user',
            email = 'user@a.com',
            password = '12221'
        )

        self.data = Product.objects.create(
            category = self.cat1,
            created_by = self.user1,
            title = 'django new',
            description = 'yeaa',
            slug = 'django-new',
            price = '20.99',
            image = 'django'

        )




    def test_product_model_entry(self):
        data = self.data
        self.assertTrue(isinstance(data, Product))
        self.assertEqual(str(data), 'django new')

    




from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse
from .models import *


class UserViewsTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.login_url = reverse('login')
        self.user_data = {
            'username': 'testuser',
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        self.user = User.objects.create_user(username='testuser', password='testpassword123')

    def test_register_view_POST(self):
        response = self.client.post(self.register_url, self.user_data)
        # self.assertEqual(response.status_code, 302)  # Redirects upon successful registration
        self.assertTrue(User.objects.filter(username='testuser').exists())

    def test_register_view_invalid_data_POST(self):
        invalid_data = {
            'username': '',  # Invalid, username cannot be empty
            'password1': 'testpassword123',
            'password2': 'testpassword123',
        }
        response = self.client.post(self.register_url, invalid_data)
        self.assertEqual(response.status_code, 200)  # Returns to the same page upon validation failure
        self.assertFalse(User.objects.filter(username='').exists())

    def test_login_view_POST(self):
        login_data = {
            'username': 'testuser',
            'password': 'testpassword123',
        }
        response = self.client.post(self.login_url, login_data, follow=True)
        self.assertRedirects(response, reverse('products'))  # Redirects to products upon successful login

    def test_login_view_invalid_data_POST(self):
        invalid_login_data = {
            'username': 'nonexistentuser',
            'password': 'wrongpassword',
        }
        response = self.client.post(self.login_url, invalid_login_data)
        self.assertFalse(response.context['user'].is_authenticated)
        self.assertContains(response, "Username OR Password is incorrect!")


#UNIT_TESTCASE FOR DASHBOARD

class ItemModelTestCase(TestCase):
    def setUp(self):
        # Create test data
        self.item1 = Item.objects.create(name="Item 1", sku="SKU001", category="Category A", tags="tag1, tag2", stock_status=10.0, available_stock=5.0)
        self.item2 = Item.objects.create(name="Item 2", sku="SKU002", category="Category B", tags="tag2, tag3", stock_status=20.0, available_stock=15.0)
        self.item3 = Item.objects.create(name="Item 3", sku="SKU003", category="Category A", tags="tag1, tag3", stock_status=30.0, available_stock=25.0)
        self.item4 = Item.objects.create(name="Item 4", sku="SKU004", category="Category C", tags="tag3, tag4", stock_status=40.0, available_stock=35.0)

    def test_search_items(self):
        # Test search functionality
        searched_items = Item.objects.filter(name__icontains='Item 1')
        self.assertEqual(len(searched_items), 1)
        self.assertEqual(searched_items[0].name, 'Item 1')

    # def test_filter_items(self):
    #     # Test filter functionality
    #     filtered_items = Item.objects.filter(category='Category A')
    #     self.assertEqual(len(filtered_items), 2)
    #     self.assertEqual(filtered_items[0].name, 'Item 1')
    #     self.assertEqual(filtered_items[1].name, 'Item 3')
        
    def test_stock_status_filter(self):
        # Test filtering items by stock status
        response = self.client.get(reverse('products'), {'stock_status': 25.0})
        self.assertEqual(response.status_code, 200)
        data = response.json()
        # Check if only items with stock status less than or equal to 25.0 are returned
        for item in data['items']:
            self.assertTrue(item['stock_status'] <= 25.0)


    def test_sort_items(self):
        # Test sort functionality
        sorted_items = Item.objects.all().order_by('name')
        self.assertEqual(len(sorted_items), 4)
        self.assertEqual(sorted_items[0].name, 'Item 1')
        self.assertEqual(sorted_items[1].name, 'Item 2')
        self.assertEqual(sorted_items[2].name, 'Item 3')
        self.assertEqual(sorted_items[3].name, 'Item 4')


# class AddItemViewTest(TestCase):
#     def setUp(self):
#         self.client = Client()

#     def test_add_item_view_POST(self):
#         # Test POST request to add a new item
#         data = {
#             'name': 'New Item',
#             'sku': 'SKU006',
#             'category': 'Category D',
#             'tags': 'tag5, tag6',
#             'stock_status': 50.0,
#             'available_stock': 4.0,
#         }
#         response = self.client.post(reverse('CreateProduct'), data=data)
        
#         # Check if item is added to the database
#         self.assertTrue(Item.objects.filter(name='New Item').exists())
        
#         # Check if user is redirected to the item dashboard upon successful addition
#         self.assertEqual(response.status_code, 302)
#         self.assertEqual(response.url, reverse('products'))

#     def test_add_item_view_invalid_data_POST(self):
        
#         # Check that the item is not added to the database
#         self.assertFalse(Item.objects.filter(name='New Item').exists())
        




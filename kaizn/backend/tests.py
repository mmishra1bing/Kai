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

#UNIT_TESTCASE FOR PASSWORDS
class PasswordResetViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()

    def test_password_reset_view(self):
        response = self.client.get(reverse('reset_password'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'backend/password_reset.html')

    def test_password_reset_sent_view(self):
        response = self.client.get(reverse('password_reset_done'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'backend/password_reset_sent.html')

    def test_password_reset_confirm_view(self):
        # Assuming we have a user in the database
        user = User.objects.create_user(username='testuser', email='test@example.com', password='testpassword')
        # Simulate a password reset request
        response = self.client.get(reverse('password_reset_confirm', args=['uidb64', 'token']))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'backend/password_reset_form.html')

    def test_password_reset_complete_view(self):
        response = self.client.get(reverse('password_reset_complete'))
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'backend/password_reset_done.html')


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

    def test_filter_items(self):
        # Test filter functionality
        filtered_items = Item.objects.filter(category='Category A')
        self.assertEqual(len(filtered_items), 2)
        self.assertEqual(filtered_items[0].name, 'Item 1')
        self.assertEqual(filtered_items[1].name, 'Item 3')
        
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



class CreateProductViewTestCase(TestCase):
    def setUp(self):
        self.client = Client()
        self.user = User.objects.create_user(username='testuser', password='testpassword')
        self.client.login(username='testuser', password='testpassword')
        self.create_product_url = reverse('CreateProduct')

    def test_create_product_view_GET(self):
        response = self.client.get(self.create_product_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'backend/create_product.html')

    def test_create_product_view_POST(self):
        initial_item_count = Item.objects.count()
        form_data = {
            'sku': 'SKU001',
            'name': 'New Product',
            'category': 'Bundles',
            'tags': 'tag15',
            'stock_status': 10.0,
            'available_stock': 5.0,
        }
        response = self.client.post(self.create_product_url, form_data)
        
        # Check if the product is added to the database
        self.assertEqual(Item.objects.count(), initial_item_count + 1)
        new_product = Item.objects.last()
        self.assertEqual(new_product.sku, 'SKU001')
        self.assertEqual(new_product.name, 'New Product')
        self.assertEqual(new_product.category, 'Bundles')
        self.assertEqual(new_product.tags, 'tag15')
        self.assertEqual(new_product.stock_status, 10.0)
        self.assertEqual(new_product.available_stock, 5.0)
        
        # Check if the view redirects to the 'products' page upon successful product creation
        self.assertRedirects(response, reverse('products'))

        




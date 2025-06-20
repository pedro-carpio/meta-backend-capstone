from django.test import TestCase
from ..models import Booking, Menu
from django.urls import reverse
from rest_framework.test import APIClient
from rest_framework import status
from ..models import Menu
from ..serializers import MenuSerializer

class MenuTest(TestCase):
    def test_get_item(self):
        item = Menu.objects.create(name="IceCream", price=80, inventory=100)
        self.assertEqual(item, "IceCream : 80")

class MenuViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.item1 = Menu.objects.create(name="Pizza", price=12, inventory=10)
        self.item2 = Menu.objects.create(name="Burger", price=8, inventory=20)
        self.item3 = Menu.objects.create(name="Salad", price=6, inventory=15)

    def test_getall(self):
        response = self.client.get(reverse('menu-list'))
        items = Menu.objects.all()
        serializer = MenuSerializer(items, many=True)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
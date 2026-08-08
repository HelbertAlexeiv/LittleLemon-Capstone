from decimal import Decimal

from django.contrib.auth.models import User
from rest_framework import status
from rest_framework.test import APITestCase

from .models import Menu


class MenuItemsViewTests(APITestCase):
	def setUp(self):
		self.user = User.objects.create_user(
			username="tester",
			password="TestPass123!",
		)
		self.client.force_authenticate(user=self.user)

	def test_create_menu_item(self):
		response = self.client.post(
			"/api/restaurant/menu/items",
			{
				"title": "Greek Salad",
				"price": "12.50",
				"inventory": 10,
			},
			format="json",
		)

		self.assertEqual(response.status_code, status.HTTP_201_CREATED)
		self.assertEqual(Menu.objects.count(), 1)

		menu_item = Menu.objects.get()
		self.assertEqual(menu_item.title, "Greek Salad")
		self.assertEqual(menu_item.price, Decimal("12.50"))
		self.assertEqual(menu_item.inventory, 10)

from model_bakery import baker
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from backend.models import User, Shop


class ShopsTests(APITestCase):

    def setUp(self) -> None:
        self.url = 'http://testserver/api/v1/shops/'
        self.customer = baker.make(Shop, _quantity=9, _bulk_create=True)

        shop_user_test1 = User.objects.create_user(email='test@test.com', password='test1test', type='shop',
                                                   is_active=True)
        self.shop_user_test1_token = Token.objects.create(user=shop_user_test1)
        user_test2 = User.objects.create_user(email='test2@test.com', password='test2test', is_active=True)
        self.user_test2_token = Token.objects.create(user=user_test2)

    def test_shops_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 9)

    def test_shop_create_unauthorized(self):
        data = {
            'name': 'test_shop'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 401)

    def test_shop_create_authorized_shop(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.shop_user_test1_token.key)
        data = {
            'name': 'test_shop1'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 201)

    def test_shop_create_authorized(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test2_token.key)
        data = {
            'name': 'test_shop2'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 403)

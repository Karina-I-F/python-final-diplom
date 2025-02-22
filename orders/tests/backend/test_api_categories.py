from model_bakery import baker
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from backend.models import User, Category


class CategoriesTests(APITestCase):

    def setUp(self) -> None:
        self.url = 'http://testserver/api/v1/categories/'
        self.customer = baker.make(Category, _quantity=5, _bulk_create=True)

        shop_user_test1 = User.objects.create_user(email='test@test.com', password='test1test', type='shop',
                                                   is_active=True)
        self.shop_user_test1_token = Token.objects.create(user=shop_user_test1)
        user_test2 = User.objects.create_user(email='test2@test.com', password='test2test', is_active=True)
        self.user_test2_token = Token.objects.create(user=user_test2)

    def test_categories_list(self):
        response = self.client.get(self.url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(len(response.data['results']), 5)

    def test_category_create_unauthorized(self):
        data = {
            'name': 'test_category'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 401)

    def test_category_create_authorized_shop(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.shop_user_test1_token.key)
        data = {
            'name': 'test_category'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 201)

    def test_category_create_authorized(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test2_token.key)
        data = {
            'name': 'test_category2'
        }
        response = self.client.post(self.url, data)

        self.assertEqual(response.status_code, 403)

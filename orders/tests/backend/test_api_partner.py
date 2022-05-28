from django.urls import reverse
from rest_framework.authtoken.models import Token
from rest_framework.test import APITestCase

from backend.models import User


class PartnerTests(APITestCase):

    def setUp(self):
        self.url_u = reverse('backend:partner-update')
        self.shop_url = 'https://raw.githubusercontent.com/netology-code/pd-diplom/master/data/shop1.yaml'

        shop_user_test1 = User.objects.create_user(email='test@test.com', password='test1test', type='shop',
                                                   is_active=True)
        self.shop_user_test1_token = Token.objects.create(user=shop_user_test1)
        user_test2 = User.objects.create_user(email='test2@test.com', password='test2test', is_active=True)
        self.user_test2_token = Token.objects.create(user=user_test2)

    def test_partner_valid_update(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.shop_user_test1_token.key)
        data = {
            'url': self.shop_url
        }
        response = self.client.post(self.url_u, data)

        self.assertEqual(response.status_code, 200)

    def test_partner_invalid_update(self):
        self.client.credentials(HTTP_AUTHORIZATION='Token ' + self.user_test2_token.key)
        data = {
            'url': self.shop_url
        }
        response = self.client.post(self.url_u, data)

        self.assertEqual(response.status_code, 403)

    def test_partner_update_unauthorized(self):
        data = {
            'url': self.shop_url
        }
        response = self.client.post(self.url_u, data)

        self.assertEqual(response.status_code, 403)

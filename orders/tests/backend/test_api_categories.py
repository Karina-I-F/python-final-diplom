import pytest
from django.urls import reverse
from rest_framework import status

from backend.models import Category


@pytest.mark.django_db
def test_category_list(api_client, categories_factory):
    categories_factory(_quantity=5)
    url = reverse('categories-list')
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert len(response.data) == 5


@pytest.mark.django_db
def test_get_category_first(api_client, categories_factory):
    categories_factory(_quantity=21)
    obj = Category.objects.first()
    url = reverse('categories-detail', kwargs={'pk': obj.id})
    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['name'] == obj.name


@pytest.mark.django_db
def test_get_category_id(api_client, categories_factory):
    categories = categories_factory(_quantity=5)
    url = f"%s{categories[3].id}/" % reverse('categories-list')

    response = api_client.get(url)

    assert response.status_code == status.HTTP_200_OK
    assert response.data['id'] == categories[3].id


@pytest.mark.django_db
def test_category_create_unauthorized(api_client):
    url = reverse('categories-list')
    payload = {
        'name': 'test_category'
    }
    response = api_client.post(url, data=payload)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_category_update_unauthorized(api_client, categories_factory):
    category = categories_factory(_quantity=1)[0]
    url = reverse('categories-detail', kwargs={'pk': category.id})
    payload = {
        'name': 'test_category'
    }
    response = api_client.put(url, data=payload)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED


@pytest.mark.django_db
def test_category_delete_unauthorized(api_client, categories_factory):
    category = categories_factory(_quantity=1)[0]
    url = reverse('categories-detail', kwargs={'pk': category.id})
    response = api_client.delete(url)

    assert response.status_code == status.HTTP_401_UNAUTHORIZED

import pytest
from model_bakery import baker
from rest_framework.test import APIClient


@pytest.fixture
def api_client():
    return APIClient()


@pytest.fixture
def shops_factory():
    def factory(**kwargs):
        return baker.make('Shop', **kwargs)
    return factory


@pytest.fixture
def categories_factory():
    def factory(**kwargs):
        return baker.make('Category', **kwargs)
    return factory

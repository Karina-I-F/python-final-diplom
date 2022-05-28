from django.urls import path, include
from django_rest_passwordreset.views import reset_password_request_token, reset_password_confirm
from rest_framework.routers import DefaultRouter

from backend.views import PartnerUpdate, PartnerState, PartnerOrders, ConfirmAccount, AccountDetails, \
    ContactView, LoginAccount, CategoryViewSet, ShopViewSet, ProductInfoViewSet, BasketView, OrderView, \
    RegisterAccountViewSet, TaskStatus

router = DefaultRouter()
router.register('user/register', RegisterAccountViewSet, basename='user-register')
router.register('shops', ShopViewSet, basename='shops')
router.register('categories', CategoryViewSet, basename='categories')
router.register('products', ProductInfoViewSet, basename='products')

app_name = 'backend'
urlpatterns = [
    path('partner/update', PartnerUpdate.as_view(), name='partner-update'),
    path('partner/state', PartnerState.as_view(), name='partner-state'),
    path('partner/orders', PartnerOrders.as_view(), name='partner-orders'),

    path('user/register/confirm', ConfirmAccount.as_view(), name='user-register-confirm'),
    path('user/details', AccountDetails.as_view(), name='user-details'),
    path('user/contact', ContactView.as_view(), name='user-contact'),
    path('user/login', LoginAccount.as_view(), name='user-login'),
    path('user/password_reset', reset_password_request_token, name='password-reset'),
    path('user/password_reset/confirm', reset_password_confirm, name='password-reset-confirm'),

    path('basket', BasketView.as_view(), name='basket'),
    path('order', OrderView.as_view(), name='order'),

    path('', include(router.urls)),

    path('task', TaskStatus.as_view(), name='task-status'),
]

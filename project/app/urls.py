from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from .views import *


urlpatterns = [
    path('', ProductList.as_view(), name='base'),
    path('product/', ProductCreate.as_view(), name='product_create'),
    path('prod/<int:pk>/uct/', ProductView.as_view(), name='prod_uct'),
    path('productmax/', ProductListMax.as_view(), name='product_max'),
    path('register/', RegistrationUserForm.as_view(), name='register'),
    path('cabinet/', cabinet, name='cabinet'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
from django.urls import path
from .views import ProductListAPI, UploadExcelAPI

urlpatterns = [
    path('upload/', UploadExcelAPI.as_view(), name='product-upload'),
    path('products/', ProductListAPI.as_view(), name='product-list'),
]
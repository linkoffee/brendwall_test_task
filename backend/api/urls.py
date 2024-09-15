from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path(
        'api/products/', views.ProductListCreate.as_view(),
        name='product-list-create'
    ),
]

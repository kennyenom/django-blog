from django.urls import path
from .import views

urlpatterns = [
    path('',views.index,name='home'),
    path('staff',views.staff,name='staff'),
    path('product',views.product,name='product'),
    path('product-edit,<int:pk>/',views.products_edit,name='products-edit'),
    path('customer detail,<int:pk>/',views.customer_detail,name='customer-detail'),
    path('product-delete,<int:pk>/',views.product_delete,name='products-delete'),
    path('order',views.order,name='order'),
    path('product_detail,<int:pk>/',views.products_detail,name='product-detail'),
]
from django.urls import path
from . import views

app_name = 'tienda'

urlpatterns = [
    path('', views.index, name='index'),
    path('productos/<int:id>/', views.product_detail, name='product_detail')
]

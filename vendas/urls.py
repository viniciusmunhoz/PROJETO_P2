from django.urls import path
from .views import list_vendas, create_vendas, update_vendas, delete_vendas

urlpatterns = [
    path('', list_vendas, name='list_vendas'),
    path('new', create_vendas, name='create_vendas'),
    path('update/<int:id>/', update_vendas, name='update_vendas'),
    path('delete/<int:id>/', delete_vendas, name='delete_vendas'),
]

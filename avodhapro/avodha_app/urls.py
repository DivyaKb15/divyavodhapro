from django.urls import path
from . import views

urlpatterns = [
    path('', views.demo, name='demo'),
    path('shop/<int:book_id>', views.details, name='details'),
    path('add/', views.add_products, name='add_products'),
    path('update/<int:id>', views.update, name='update'),
    path('delete/<int:id>', views.delete, name='delete'),
]

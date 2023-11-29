from django.contrib import admin
from django.urls import path
from home import  views

urlpatterns = [
    path('admin/', admin.site.urls),

    path('', views.list_todos, name='todos-item'),

    path('item-criar/', views.list_criar, name='criar-item'),

    path('item-pegar/<int:pk>/', views.list_pegar, name='pegar-item'),

    path('item-atualizar/<int:pk>/', views.list_atualizar, name='atualizar-item'),

    path('item-deletar/<int:pk>/', views.list_deletar, name='deletar-item'),
]

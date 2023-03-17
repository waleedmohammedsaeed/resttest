from django.urls import path
from . import views



urlpatterns = [
    path('', views.todo),
    path('action/<int:id>/', views.action, name='action')
]
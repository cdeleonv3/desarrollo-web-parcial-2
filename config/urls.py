
from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.videos, name='videos'),
    path('users/', views.users, name='users'),
    path('credits/', views.credits, name='credits'),
]

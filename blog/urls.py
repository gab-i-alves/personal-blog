from django.urls import path
from . import views

app_name = 'blog'   # URL namespacing

urlpatterns = [
    path('', views.home, name='home'),
]
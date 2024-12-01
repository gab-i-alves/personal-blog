from django.urls import path
from . import views

app_name = 'blog'   # URL namespacing

urlpatterns = [
    path('', views.home, name='home'),
    path('article/<int:id>/', views.article_detail, name='article_detail')
]
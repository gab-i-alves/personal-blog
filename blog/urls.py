from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = 'blog'   # URL namespacing

urlpatterns = [
    # Guest Section
    path('', views.home, name='home'),
    path('article/<int:id>/', views.article_detail, name='article_detail'),

    # Admin Section
    path('manage/dashboard/', views.dashboard, name='dashboard'),
    path('manage/add-article/', views.add_article, name='add_article'),
    path('manage/edit-article/<int:id>/', views.edit_article, name='edit_article'),
    path('manage/delete-article/<int:id>/', views.delete_article, name='delete_article'),
    
    # Authentication - Updated template paths to match folder structure
    path('manage/login/', 
         auth_views.LoginView.as_view(template_name='blog/admin/login.html'), 
         name='login'),
    path('manage/logout/', 
         auth_views.LogoutView.as_view(next_page='blog:home'), 
         name='logout'),
]
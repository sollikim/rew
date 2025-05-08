from django.urls import path
from .views import PostListCreate, PostRetrieveUpdateDestroy
from django.urls import path
from . import views
from django.contrib.auth import views as auth_views
from django.views.generic.base import RedirectView



urlpatterns = [
    path('posts/', PostListCreate.as_view(), name='post-list-create'),
    path('posts/<int:pk>/', PostRetrieveUpdateDestroy.as_view(), name='post-retrieve-update-destroy'),
    path('', views.home, name='home'),  # Главная страница
    path('about/', views.about, name='about'),  # Страница "О нас"
    path('posts/', views.post_list, name='post-list'),
    path('comments/', views.CommentListCreate.as_view(), name='comment-list-create'),
]



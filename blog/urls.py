from django.urls import path
from . import views


urlpatterns = [
    path('', views.all_blog, name='blog'),
    path('<int:blog_id>/', views.blog_post, name='blog_post'),
    path('add/', views.add_post, name='add_post'),
]

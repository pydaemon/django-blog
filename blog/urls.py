from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

urlpatterns = [
    path('', views.PostListView.as_view(), name='post_list'),
    path("category/<slug:slug>/", views.CategoryListView.as_view(), name='category_list'),
    path('post/new/', views.PostCreateView.as_view(), name='post_new'),
    path('post/<slug:slug>/', views.PostDetailView.as_view(), name='post_detail'),
    path('post/<slug:slug>/edit/', views.PostUpdateView.as_view(), name='post_edit'),
    path('post/<slug:slug>/comment/', views.CommentCreateView.as_view(), name='comment_new'),
    path('login/', auth_views.LoginView.as_view(template_name='blog/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='post_list'), name='logout'),
    path('register/', views.register, name='register'),
]
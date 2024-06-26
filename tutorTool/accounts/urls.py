from django.contrib.auth import views as auth_views
from django.urls import path
from . import views

app_name = "accounts"

urlpatterns = [
    # path('', views.PostListView.as_view(), name='post_list'),
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('signup/', views.SignUp.as_view(), name='signup'),
    # path('post/<int:pk>/', views.PostDetailView.as_view(), name='post_detail'),
]
from django.urls import path
from .views import user_registration, user_login, user_profile, user_change_password, create_post, list_user_posts
from rest_framework_simplejwt.views import TokenRefreshView

urlpatterns = [
    path('register/', user_registration, name='user-register'),
    path('login/', user_login, name='user-login'),
    path('profile/', user_profile, name='user-profile'),
    path('change-password/', user_change_password, name='user-change-password'),
    path('posts/create/', create_post, name='create-post'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('posts/', list_user_posts, name='user-posts'),
]
from django.urls import path

from .views import (create_post, create_user, get_posts, get_users, like_post,
                    user_detail)

urlpatterns = [
    path('users/', get_users, name='get_user'),
    path('posts/', get_posts, name='get_posts'),
    path('users/create/', create_user, name='create_user'),
    path('posts/create/', create_post, name='create_post'),
    path('posts/<int:post_id>/like', like_post, name='like_post'),
    path('users/<int:pk>', user_detail, name='user_detail'),
]

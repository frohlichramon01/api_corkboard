from rest_framework import serializers

from .models import Post, User


class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = Post
        fields = ['id',
                  'author',
                  'created_at',
                  'subject',
                  'content',
                  'likes']

class UserSerializer(serializers.ModelSerializer):
    posts = PostSerializer(many=True, read_only=True)

    class Meta:
        model = User
        fields = ['id',
                  'username',
                  'created_at',
                  'department',
                  'posts']

        

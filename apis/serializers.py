from django.contrib.auth import get_user_model
from rest_framework import serializers

from blog.models import Post, Category


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")
    category = serializers.SlugRelatedField(
        queryset=Category.objects.all(),
        required=False,
        allow_null=True,
        slug_field="name",
    )

    class Meta:
        model = Post
        fields = (
            "id",
            "title",
            "subtitle",
            "author",
            "body",
            "publish",
            "category",
        )


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = (
            "id",
            "username",
        )

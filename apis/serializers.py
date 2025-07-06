from rest_framework import serializers

from blog.models import Post


class PostSerializer(serializers.ModelSerializer):
    author = serializers.SlugRelatedField(read_only=True, slug_field="username")
    category = serializers.SlugRelatedField(read_only=True, slug_field="name")

    class Meta:
        model = Post
        fields = ("id", "title", "subtitle", "author", "body", "date", "category")

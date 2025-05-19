from http.client import responses

from django.test import TestCase
from django.contrib.auth.models import User
from .models import Post, Category

class BlogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.category = Category.objects.create(name="Test Category")
        self.post = Post.objects.create(
            title="Test Post",
            body="This is a test post.",
            author=self.user,
            category=self.category,
        )

    def test_post_model(self):
        self.assertEqual(str(self.post), "Test Post")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.category.name, "Test Category")

    def test_post_list_view(self):
        response = self.client.get("/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_post_detail_view(self):
        response = self.client.get(f"/post/{self.post.pk}/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertTemplateUsed(response, "blog/post_detail.html")
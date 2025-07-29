from django.contrib.auth import get_user_model
from django.test import TestCase
from django.urls import reverse
from django.utils.text import slugify

from .models import Post, Category


class PostTests(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234",
        )

        cls.category = Category.objects.create(name="testcategory")

        cls.post = Post.objects.create(
            category=cls.category,
            title="Test Post",
            subtitle="Test Subtitle",
            author=cls.user,
            body="This is a test post",
            slug=slugify("Test Post"),
            status=Post.Status.PUBLISHED,
        )

    def test_post_content(self):
        self.assertEqual(self.post.category.name, "testcategory")
        self.assertEqual(self.post.title, "Test Post")
        self.assertEqual(self.post.subtitle, "Test Subtitle")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.body, "This is a test post")
        self.assertEqual(str(self.post), "Test Post")

    def test_post_listview(self):
        response = self.client.get(reverse("home"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertTemplateUsed(response, "home.html")

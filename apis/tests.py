from django.contrib.auth import get_user_model
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase

from blog.models import Post, Category


class APITests(APITestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = get_user_model().objects.create_user(
            username="testuser",
            email="testuser@example.com",
            password="testpass1234",
        )

        cls.category = Category.objects.create(name="testcategory")

        cls.post = Post.objects.create(
            title="Test Post",
            subtitle="Test Subtitle",
            body="This is a test post",
            author=cls.user,
            category=cls.category,
        )

    def test_api_listview(self):
        response = self.client.get(reverse("post_list_api"))
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(response, self.post)

    def test_api_detailview(self):
        response = self.client.get(
            reverse("post_detail_api", kwargs={"pk": self.post.id}), format="json"
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(Post.objects.count(), 1)
        self.assertContains(response, "Test Post")

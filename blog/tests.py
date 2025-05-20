from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse
from .models import Post, Category, Comment

class BlogTests(TestCase):
    def setUp(self):
        self.user = User.objects.create_user(
            username="testuser", password="testpass123"
        )
        self.category = Category.objects.create(name="Test Category", slug="test-category")
        self.post = Post.objects.create(
            title="Test Post",
            slug="test-post",
            body="This is a test post.",
            author=self.user,
            category=self.category,
        )
        self.comment = Comment.objects.create(
            post=self.post,
            author=self.user,
            body="This is a test comment.",
        )

    def test_post_model(self):
        self.assertEqual(str(self.post), "Test Post")
        self.assertEqual(self.post.author.username, "testuser")
        self.assertEqual(self.post.category.name, "Test Category")
        self.assertEqual(self.post.slug, "test-post")

    def test_comment_model(self):
        self.assertEqual(str(self.comment), f"Comment by {self.user} on {self.post}")
        self.assertEqual(self.comment.post, self.post)

    def test_post_list_view(self):
        response = self.client.get(reverse("post_list"))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_category_list_view(self):
        response = self.client.get(reverse("category_list", kwargs={"slug": "test-category"}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertTemplateUsed(response, "blog/post_list.html")

    def test_post_detail_view(self):
        response = self.client.get(reverse("post_detail", kwargs={"slug": "test-post"}))
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "Test Post")
        self.assertContains(response, "This is a test comment.")
        self.assertTemplateUsed(response, "blog/post_detail.html")

    def test_comment_create_view(self):
        self.client.login(username="testuser", password="testpass123")
        response = self.client.post(
            reverse("comment_new", kwargs={"slug": "test-post"}),
            {'body': 'New comment'},
        )
        self.assertEqual(response.status_code, 302)
        self.assertEqual(Comment.objects.last().body, "New comment")
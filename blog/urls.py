from django.urls import path
from .views import (
    BlogListView,
    BlogDetailView,
    BlogUpdateView,
    BlogDeleteView,
    BlogCreateView,
    post_share,
)

urlpatterns = [
    path(
        "post/<int:year>/<int:month>/<int:day>/<slug:post>/",
        BlogDetailView.as_view(),
        name="post_detail",
    ),
    path("post/<int:pk>/edit/", BlogUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BlogDeleteView.as_view(), name="post_delete"),
    path("post/<int:post_id>/share/", post_share, name="post_share"),
    path("post/new/", BlogCreateView.as_view(), name="post_new"),
    path("", BlogListView.as_view(), name="home"),
]

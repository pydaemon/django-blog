from django.urls import path

from .views import PostList, PostDetail

urlpatterns = [
    path("<int:pk>/", PostDetail.as_view(), name="post_detail_api"),
    path("", PostList.as_view(), name="post_list_api"),
]

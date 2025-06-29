from django.contrib import admin
from .models import Category, Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


class PostAdmin(admin.ModelAdmin):
    def body(obj):
        return obj.body[:50] + "..."

    inlines = [CommentInline]
    list_display = [
        "title",
        "author",
        body,
        "category",
    ]


admin.site.register(Category)
admin.site.register(Post, PostAdmin)
admin.site.register(Comment)

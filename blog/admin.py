from django.contrib import admin
from .models import Category, Post, Comment


class CommentInline(admin.TabularInline):
    model = Comment
    extra = 0


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    inlines = [CommentInline]
    list_display = [
        "title",
        "slug",
        "author",
        "publish",
        "status",
        "category",
    ]
    list_filter = ["status", "created_at", "publish", "author", "category"]
    search_fields = ["title", "body"]
    prepopulated_fields = {"slug": ("title",)}
    raw_id_fields = ["author"]
    date_hierarchy = "publish"
    ordering = ["status", "publish"]
    show_facets = admin.ShowFacets.ALWAYS


admin.site.register(Category)
admin.site.register(Comment)

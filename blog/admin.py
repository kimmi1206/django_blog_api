from django.contrib import admin

from .models import Post, Author, Tag  # pylint: disable=no-name-in-module

# Register your models here.


class PostAdmin(admin.ModelAdmin):
    list_filter = ("author", "tags", "date",)
    list_display = ("title", "excerpt", "author", "date",)
    prepopulated_fields = {"slug": ("title",)}


admin.site.register(Post, PostAdmin)
admin.site.register(Author)
admin.site.register(Tag)

from django.contrib import admin
from .models import Post, Article, Publication
# Register your models here.

admin.site.register(Post)
admin.site.register(Publication)
admin.site.register(Article)


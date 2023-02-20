from django.contrib import admin

from .models import Article, Scope, Tag


class ScopeInline(admin.TabularInline):
    model = Scope
    extra = 1


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

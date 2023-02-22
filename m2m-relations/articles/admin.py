from django.contrib import admin
from django.forms.models import BaseInlineFormSet
from django.core.exceptions import ValidationError


from .models import Article, Scope, Tag


class ScopeInlineFormSet(BaseInlineFormSet):
    def clean(self):
        main_check = tuple(
            form.cleaned_data.get('is_main') for form in self.forms
        )
        print(main_check)
        if main_check.count(True) < 1:
            raise ValidationError('Выберите основной раздел.')
        elif main_check.count(True) > 1:
            raise ValidationError('Основным разделом может быть только один.')
        super(ScopeInlineFormSet, self).clean()


class ScopeInline(admin.TabularInline):
    print("SCOPE inline")
    model = Scope
    extra = 1
    formset = ScopeInlineFormSet


@admin.register(Article)
class ArticleAdmin(admin.ModelAdmin):
    print("ADMIN article")
    inlines = [ScopeInline]


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    pass

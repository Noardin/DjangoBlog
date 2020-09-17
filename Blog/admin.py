from django.contrib import admin
from django.contrib.auth.models import User
from django import forms
from django.contrib.admin import AdminSite
# Register your models here.
from .models import Articles


class ArticlesForm(forms.ModelForm):
    class Meta:
        model = Articles
        fields = '__all__'
        def clean_author(self):
            if not self.cleaned_data['article_author']:
                return User()
            return self.cleaned_data['article_author']

@admin.register(Articles)
class BlogAdmin(admin.ModelAdmin):
    form = ArticlesForm

    list_display = ('article_text', 'article_header', 'article_author')
    readonly_fields = ['pub_date']
    exclude = ['article_author']

    def get_queryset(self, request):
        queryset=super().get_queryset(request)
        if request.user.is_superuser:
            return queryset
        return queryset.filter(article_author=request.user)

    def save_model(self, request, obj, form, change):
        if not obj.article_author:
            obj.article_author = request.user
        obj.save()
class BlogAdminSite(AdminSite):

    AdminSite.site_url = '/blog'



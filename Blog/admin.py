from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin
from django.contrib.auth.forms import UserCreationForm
from django import forms
from django.contrib.admin import AdminSite
# Register your models here.
from .models import Articles, Profile


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


class ProfileInline(admin.StackedInline):
    model = Profile
    can_delete = False
    verbose_name_plural = 'Profile'
    fk_name = 'user'

class CustomUserAdmin(UserAdmin):
    inlines = (ProfileInline, )

    def get_inline_instances(self, request, obj=None):
        if not obj:
            return list()
        return super(CustomUserAdmin, self).get_inline_instances(request, obj)

admin.site.unregister(User)
admin.site.register(User, CustomUserAdmin)

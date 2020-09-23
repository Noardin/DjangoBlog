from django.urls import path, include,re_path
from . import views

urlpatterns = [
    path('<int:article_id>', views.articles, name= "article"),
    re_path(r'^(?P<article_id>[0-9]{1,4})/(?P<expand_comments>true|false)', views.articles, name="article_comment"),
    path('', views.articles, name="articles"),
    path('addcomment/<int:article_id>', views.add_comment, name="add_comment"),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signUp',views.sign_up, name="signUp")
]

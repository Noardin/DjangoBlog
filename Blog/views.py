from django.shortcuts import render, redirect
from .models import Articles, Comments
from django.contrib.auth.forms import UserCreationForm
from .blogForms import ProfileForm

def articles(request, article_id =0, expand_comments='false'):

    articles_list= Articles.objects.all()
    print(expand_comments)
    if(article_id == 0):
        articles_list = articles_list.order_by('-pub_date')
        context = {'article_list': articles_list}
        return render(request, 'blog/article.html', context=context)
    article = articles_list.get(pk=article_id)
    comment_list = Comments.objects.all()
    context = {'article': article, 'expand_comments': expand_comments, 'comments': comment_list}
    return render(request, 'blog/article_detail.html', context= context)

def add_comment(request):
    if request.method == "POST":
        Article = Articles.objects.get(pk=request.POST['article_id'])
        Comment = Comments(comment_author=request.user, comment_article=Article, comment_text=request.POST['comment_text'])
        Comment.save()
    return redirect(articles,article_id=request.POST["article_id"], expand_comments='true')

def sign_up(request):
    if request.method == "POST":
        userCreationForm = UserCreationForm(request.POST["userCreationForm"])
        profileForm = ProfileForm(request.POST["profileForm"])
        context = {
            "userCreationForm": userCreationForm,
            "profileForm":profileForm
        }
        render(request, 'registration/signUp.html', context)
    else:
        render(request, 'registration/signUp.html')
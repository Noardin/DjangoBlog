from django.shortcuts import render
from .models import Articles, Comments

def articles(request, article_id =0, expand_comments='false'):

    articles_list= Articles.objects
    print(expand_comments)
    if(article_id == 0):
        articles_list = articles_list.order_by('-pub_date')
        context = {'article_list': articles_list}
        return render(request, 'blog/article.html', context=context)
    article = articles_list.get(pk=article_id)
    context = {'article': article, 'expand_comments': expand_comments}
    return render(request, 'blog/article_detail.html', context= context)

def add_comment(request):
    if request.method == "POST":
        Article = Articles.objects.get(pk=request.POST['article_id'])
        Comment = Comments(comment_author=request.user, comment_article=Article, comment_text=request.POST["comment_text"])
    return articles(request)
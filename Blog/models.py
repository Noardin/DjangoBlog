from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Articles(models.Model):
    article_author = models.ForeignKey(User, on_delete=models.CASCADE,null=True, blank=True)
    article_header = models.CharField(max_length=30)
    article_text = models.TextField(default='here comes text')
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.article_header

class Comments(models.Model):
    comment_author = models.ForeignKey(User, on_delete= models.CASCADE, blank=True)
    comment_article = models.ForeignKey(Articles, on_delete=models.CASCADE, blank=True)
    comment_text = models.TextField(default="comment on article...")
    pub_date = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.comment_text
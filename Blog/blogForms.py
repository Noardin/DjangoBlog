from django.forms import ModelForm
from .models import Comments

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text','pub_date','comment_author','comment_article']
from django.forms import ModelForm
from .models import Comments, Profile

class CommentForm(ModelForm):
    class Meta:
        model = Comments
        fields = ['comment_text','comment_author','comment_article']

class ProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = ['profile_image']
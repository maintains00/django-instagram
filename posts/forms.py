from django import forms
from posts.models import Post
from django.core.exceptions import ValidationError


# class PostBaseForm(forms.Form):
#     CATEGORY_CHOICES = [
#         ('1', '일반'),
#         ('2', '계정'),
#     ]
#     image = forms.ImageField(label="이미지")
#     content = forms.CharField(label="내용", widget=forms.Textarea, required=True)
#     category = forms.ChoiceField(label="카테고리", choices=CATEGORY_CHOICES)
    
    
class PostBaseForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = '__all__'
        
class PostCreateForm(PostBaseForm):
    class Meta(PostBaseForm.Meta):
        fields = ['image', 'content']
        
        # def clean_content(self):
        #     data = self.cleaned_data['content']
        #     if "비속어" == data:
        #         raise ValidationError("'비속어'는 사용하실 수 없습니다.")
        #     return data;
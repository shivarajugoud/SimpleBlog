from django import forms
from django.forms.fields import ChoiceField
from .models import Post,Category
# choices = [('coding','coding'),('sports','sports'),('entertainment','entertainment')]
#This way we need to restart the server again
choices = Category.objects.all().values_list('name','name')
choice_list = []
for item in choices:
    choice_list.append(item)
class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields =('title','author','category','body')
        widgets = {
            'title': forms.TextInput(attrs={'class':'form-control'}),
            'author': forms.TextInput(attrs={'class':'form-control','value':'','id':'elder','type':'hidden'}),
            # 'author': forms.Select(attrs={'class':'form-control'}),
            'category': forms.Select(choices=choice_list,attrs={'class':'form-control'}),
            # 'category': forms.Select(attrs={'class':'form-control'}),
            'body': forms.Textarea(attrs={'class':'form-control'})
        }
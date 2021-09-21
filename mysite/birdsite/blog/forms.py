from django import forms
from .models import Bird


class EmailPostForm(forms.Form):
    name = forms.CharField(max_length=25)
    email = forms.EmailField()
    to = forms.EmailField()
    comments = forms.CharField(required=False,
                               widget=forms.Textarea)


class BirdForm(forms.ModelForm):
    class Meta:
        model = Bird
        fields = ('name',)


class SearchForm(forms.Form):
    query = forms.CharField()

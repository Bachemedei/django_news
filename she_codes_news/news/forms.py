from django import forms
from django.forms import ModelForm
from django.utils.translation import ugettext_lazy as _
from .models import NewsStory


class StoryForm(ModelForm):
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content', 'image']
        labels = {
            'image' : _('Image (URL)'),
            'pub_date' : _('Publication Date')
        }
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'title-input',
                'id' : 'title-label'
                }),
            'author': forms.TextInput(attrs={'class': 'author-input'}),
            'pub_date': forms.DateTimeInput(
                format=('%Y-%m-%d %H:%M'),
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Select a date',
                    'type': 'date'
                }
            ),
            'content': forms.Textarea(attrs={'class': 'content-input'}),
            'image': forms.URLInput(attrs={'class': 'image-input'})
        }

from django import forms
from django.forms import ModelForm, SplitDateTimeField, SplitDateTimeWidget
from django.utils.translation import ugettext_lazy as _

from .models import NewsStory


class StoryForm(ModelForm):
    pub_date = SplitDateTimeField(
        widget = SplitDateTimeWidget(
            date_attrs={'type': 'date'},
            time_attrs={'type': 'time'},
        )   
    )
    class Meta:
        model = NewsStory
        fields = ['title', 'author', 'pub_date', 'content', 'image']
        labels = {
            'image' : _('Image (URL)'),
        }


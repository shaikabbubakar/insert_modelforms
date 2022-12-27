from app.models import *
from django import forms
class TopicForm(forms.ModelForm):
    class Meta:
        model=Topic
        fields='__all__'
class WebpageForm(forms.ModelForm):
    class Meta:
        model=webpage
        fields='__all__'
        #fields=['topic_name','url']
        #exclude=['name']
        help_texts={'topic_name':'should not be integers','name':'only Alphabets'}
        #labels={'topic_name':'TN','name':'N'}
        #widgets={'url':forms.PasswordInput,'name':forms.Textarea}
class AccessrecordsForm(forms.ModelForm):
    class Meta:
        model=Access_records
        fields='__all__'
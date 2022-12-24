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
class AccessrecordsForm(forms.ModelForm):
    class Meta:
        model=Access_records
        fields='__all__'
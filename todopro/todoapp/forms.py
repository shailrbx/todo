from django import forms
from .models import task

class taskeform(forms.ModelForm):
    class Meta:
        model=task
        fields=['name','prio','date']

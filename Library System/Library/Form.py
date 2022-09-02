from django import forms
from .models import Students, Book, Book_Issue

class StForm(forms.ModelForm):
    class Meta:
        model = Students
        fields = '_all_'

class BkForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = '__all__'

class BIssueForm(forms.ModelForm):
    class Meta:
        model = Book_Issue
        fields = '_all_'
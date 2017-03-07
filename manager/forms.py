from django.contrib.auth.models import User
from django import forms

class BudgetForm(forms.ModelForm):

    class Meta:
        fields = ['budget_title','budget_total']

class Section(forms.ModelForm):

    class Meta:
        fields = ['section_title','section_total']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

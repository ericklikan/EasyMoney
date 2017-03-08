from django.contrib.auth.models import User
from .models import Section, Budget
from django import forms

class BudgetForm(forms.ModelForm):

    class Meta:
        model = Budget
        fields = ['budget_title','budget_total']

class SectionForm(forms.ModelForm):

    class Meta:
        model = Section
        fields = ['section_title','section_budget']

class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ['username','email','password']

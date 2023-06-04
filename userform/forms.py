from django import forms
from userform.models import UserForm

class UserFormForm(forms.ModelForm):
    class Meta:
        model = UserForm
        fields = '__all__'

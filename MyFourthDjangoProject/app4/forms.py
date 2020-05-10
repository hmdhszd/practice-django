from django import forms
from app4.models import User

class NewUserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = '__all__'
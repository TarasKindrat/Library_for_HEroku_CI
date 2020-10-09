from django import forms
from .models import CustomUser

class NewCustomUserForm(forms.ModelForm):
    # message = forms.CharField(widget=forms.Textarea(), max_length=4000)

    class Meta:
        model = CustomUser
        fields = ['first_name', 'middle_name', 'last_name', 'email', 'password', 'role', 'is_active']
        labels = {'role': '0 - visitor or 1 - admin',
                  'is_active': '0 - not active or 1 - active'}
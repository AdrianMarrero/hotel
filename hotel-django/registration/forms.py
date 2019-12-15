from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

class UserCreationFormWithEmail(UserCreationForm):
    email = forms.EmailField(required=True, help_text='Campo requerido')

    class Meta:
        model = User
        fields = {'username', 'password1', 'password2', 'email'}

    def clean_email(self):
        email = self.cleaned_data.get('email')
        if User.objects.filter(email=email).exists():
            raise forms.ValidationError('Este email pertenece a otro usuario')
        return email

    field_order = ['username', 'password1', 'password2', 'email']

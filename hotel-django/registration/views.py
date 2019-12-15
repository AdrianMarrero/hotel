from .forms import UserCreationFormWithEmail
from django.views.generic import CreateView
from django.urls import reverse_lazy
from django import forms

# Create your views here.
class SignUpView(CreateView):
    form_class = UserCreationFormWithEmail
    template_name = 'registration/signup.html'

    def get_success_url(self):
        return  reverse_lazy('login') + '?registrado'

    def get_form(self, form_class=None):
        form = super(SignUpView, self).get_form()

        form.fields['username'].widget = forms.TextInput(attrs={'class':'form-control mb2', 'placeholder':'Nombre', 'tabindex':'1'})
        form.fields['password1'].widget = forms.PasswordInput(attrs={'class':'form-control mb2', 'placeholder':'Contraseña', 'tabindex':'2'})
        form.fields['password2'].widget = forms.PasswordInput(attrs={'class':'form-control mb2', 'placeholder':'Confirmar contraseña','tabindex':'3'})
        form.fields['email'].widget = forms.EmailInput(attrs={'class':'form-control mb2', 'placeholder':'Email','tabindex':'4'})
        return form
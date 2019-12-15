from django import forms
from .models import Book

class BookForm(forms.ModelForm):
    
    
    class Meta:
        model = Book

        fields = [
            'date_start',
            'date_end',
            'days',
            'n_persons',
            'total_price',
            'name',
            'surname',
            'email',
            'name_of_card',
            'credit_card_number',
            'notes',
        ]

        widgets = {
            'date_start': forms.DateInput(format='%d/%m/%Y', attrs={'class':'form-control', 'readonly':'readonly'}),
            'date_end': forms.DateInput(format='%d/%m/%Y', attrs={'class':'form-control', 'readonly':'readonly'}),
            'days': forms.TextInput(attrs={'class':'form-control'}),
            'n_persons': forms.TextInput(attrs={'class':'form-control col-md-2', 'readonly':'readonly'}),
            'total_price': forms.TextInput(attrs={'class':'form-control', 'readonly':'readonly'}),
            'name': forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
            'surname': forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
            'email': forms.EmailInput(attrs={'class':'form-control', 'required':'required'}),
            'name_of_card': forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
            'credit_card_number': forms.TextInput(attrs={'class':'form-control', 'required':'required'}),
            'notes': forms.Textarea(attrs={'class':'form-control', 'rows':3, 'placeholder':'Notas'}),
       }
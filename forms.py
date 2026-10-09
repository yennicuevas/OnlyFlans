
from django import forms
from .models import ContactForm

class ContactFormModelForm(forms.ModelForm):
    class Meta:
            model = ContactForm
            fields = ['customer_email', 'customer_name', 'message']
            labels = {
                'customer_email': 'Correo Electrónico',
                'customer_name': 'Nombre Completo',
                'message': 'Mensaje o Sugerencia'
            }
            widgets = {
                'customer_email': forms.EmailInput(attrs={'class': 'form-control'}),
                'customer_name': forms.TextInput(attrs={'class': 'form-control'}),
                'message': forms.Textarea(attrs={'class': 'form-control', 'rows': 4}),
            }
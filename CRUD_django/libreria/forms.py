from django import forms
from .models import Libro

class LibroForm(forms.ModelForm):
    class Meta:
        model = Libro
        fields = '__all__' # debe recibir lista de fields, pero de esta forma le damos todo.
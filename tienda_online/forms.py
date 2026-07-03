from django import forms
from .models import Producto


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Producto
        fields = ['nombre', 'descripcion', 'precio', 'stock', 'disponible']

        widgets = {
            'nombre': forms.TextInput(attrs={'class': 'form-control'}),
            'descripcion': forms.Textarea(attrs={'class': 'form-control', 'rows': 3}),
            'precio': forms.NumberInput(attrs={'class': 'form-control', 'min': 1}),
            'stock': forms.NumberInput(attrs={'class': 'form-control', 'min': 0}),
            'disponible': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
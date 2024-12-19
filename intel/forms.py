from django import forms

class ProductForms(forms.Form):
    name = forms.CharField(max_length=100)
    price = forms.FloatField()
    stock = forms.BooleanField(required=False) #required IGUAL a Falso indica que el campo 'stock' no es obligatorio. Esto a raíz de que por default=True



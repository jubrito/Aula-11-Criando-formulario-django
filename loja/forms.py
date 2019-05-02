from django import forms
from loja.models import Pedido #nao cadastrar produto, apenas pedido

class PedidoForm(forms.ModelForm):
    class Meta:
        model = Pedido 
        #campos do formulario
        fields = [
            'nome',
            'email',
            'endereco',
            'cartao',
            'pagamento'
        ]


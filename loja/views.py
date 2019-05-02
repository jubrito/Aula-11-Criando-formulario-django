from django.shortcuts import render
from loja.forms import PedidoForm

# Create your views here.
def fazer_pedido(request):

    #ENTRAR PELA PRIMEIRA VEZ NO SITE USA METODO REQUEST.GET
    #ENTRA PELO CLICK ENVIANDO O FORMULARIO USA O METODO REQUEST.POST)  
    formulario = PedidoForm(request.POST or None)
    msg = ''
    if formulario.is_valid():
        formulario.save()
        formulario = PedidoForm() #depois de enviar, apaga
        msg = 'Pedido realizado com sucesso'

    contexto = {
        'form' : formulario,
        'msg' : msg
    }

    #CONTEXTO: MANDA COISAS DO PYTHON PRO HTML (ACESSA FORMULARIO DO BACKEND PRO FRONTEND)
    return render(request, 'index.html', contexto)
from django.contrib import admin
from loja.models import Pedido, Produto
# Register your models here.


#~~~~~~~~~~~~~~~~~~~~~REGISTRA NA PARTE DE ADMIN OS OBJ~~~~~~~~~~~~~~~~~~~~~
admin.site.register(Pedido)
admin.site.register(Produto)
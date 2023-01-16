from django.contrib import admin
from .models import (Marca, 
    Veiculo, 
    Pessoa, 
    Parametros, 
    MovimentoRotativo,
    Mensalista,
    MovMensalista)


class MovimentoRotativoAdmin(admin.ModelAdmin):
    list_display = (
        'entrada', 'saida', 'valor_hora', 'pago',
        'total', 'hora_total','veiculo')
    
    '''def veiculo(self, obj):
        return obj.veiculo'''

class MovMensalistaAdmin(admin.ModelAdmin):
    list_display = (
        'mensalista', 'dt_pgto', 'total'
    )

# Register your models here.

admin.site.register(Marca)
admin.site.register(Veiculo)
admin.site.register(Pessoa)
admin.site.register(Parametros)
admin.site.register(MovimentoRotativo, MovimentoRotativoAdmin)
admin.site.register(Mensalista)
admin.site.register(MovMensalista)
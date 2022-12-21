from django.contrib import admin
from .models import Empregado, Telefone, CPF, Departamento
# Register your models here.

admin.site.register(Empregado)
admin.site.register(Telefone)
admin.site.register(CPF)
admin.site.register(Departamento)
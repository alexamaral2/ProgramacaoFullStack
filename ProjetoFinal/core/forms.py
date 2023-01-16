from django.forms import ModelForm
from .models import (
    Pessoa, 
    Veiculo,
    MovimentoRotativo,
    Mensalista,
    MovMensalista
    )

class PessoaForm(ModelForm):
    class Meta:
        model = Pessoa
        fields = '__all__'

class VeiculoForm(ModelForm):
    class Meta:
        model = Veiculo
        fields = '__all__'

class MovimentoRotativoForm(ModelForm):
    class Meta:
        model = MovimentoRotativo
        fields = '__all__'

class MensalistaForm(ModelForm):
    class Meta:
        model = Mensalista
        fields = '__all__'

class MovMensalistaForm(ModelForm):
    class Meta:
        model = MovMensalista
        fields = '__all__'
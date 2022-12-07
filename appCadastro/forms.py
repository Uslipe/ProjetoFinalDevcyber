from django import forms
from .models import Produto

class CadastrarProduto(forms.ModelForm):

    class Meta:
        model = Produto
        fields =    ('tipo_produto',
                    'marca_produto',
                    'descricao_produto',
                    'data_cadastro',
                    'preco_compra',
                    'preco_venda')
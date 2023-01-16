from django.urls import re_path
from .views import (
    home, 
    lista_pessoas, 
    lista_veiculos,
    lista_movrotativos,
    movrotativos_novo,
    lista_mensalista,
    lista_movmensalista,
    pessoa_novo,
    veiculo_novo,
    mensalista_novo,
    movmensalista_novo,
    pessoa_update,
    veiculo_update,
    movrotativo_update,
    mensalista_update,
    movmensalista_update,
    pessoa_delete,
    veiculo_delete,
    movrotativo_delete,
    mensalista_delete,
    movmensalista_delete
)

urlpatterns = [
    re_path(r'^$', home, name='core_home'),
    re_path(r'^pessoas/$', lista_pessoas, name='core_pessoas'),
    re_path(r'^pessoas-novo/$', pessoa_novo, name='core_pessoas_novo'),
    re_path(r'^pessoas-update/(?P<id>\d+)\$', pessoa_update, name='core_pessoas_update'),
    re_path(r'^pessoas-delete/(?P<id>\d+)\$', pessoa_delete, name='core_pessoas_delete'),

    re_path(r'^veiculos/$', lista_veiculos, name='core_veiculos'),
    re_path(r'^veiculos-novo/$', veiculo_novo, name='core_veiculos_novo'),
    re_path(r'^veiculos-update/(?P<id>\d+)\$', veiculo_update, name='core_veiculo_update'),
    re_path(r'^veiculos-delete/(?P<id>\d+)\$', veiculo_delete, name='core_veiculo_delete'),

    re_path(r'^mov-rotativo/$', lista_movrotativos, name='core_movimento_rotativo'),
    re_path(r'^mov-rotativo-novo/$', movrotativos_novo, name='core_movimento_rotativo-novo'),
    re_path(r'^mov-rotativo-update/(?P<id>\d+)\$', movrotativo_update, name='core_movimento_rotativo_update'),
    re_path(r'^mov-rotativo-delete/(?P<id>\d+)\$', movrotativo_delete, name='core_movimento_rotativo_delete'),

    re_path(r'^mensalistas/$', lista_mensalista, name='core_mensalista'),
    re_path(r'^mensalistas-novo/$', mensalista_novo, name='core_mensalista-novo'),
    re_path(r'^mensalistas-update/(?P<id>\d+)\$', mensalista_update, name='core_mensalista_update'),
    re_path(r'^mensalista-delete/(?P<id>\d+)\$', mensalista_delete, name='core_mensalista_delete'),

    re_path(r'^mov-mensalista/$', lista_movmensalista, name='core_movimento_mensalista'),
    re_path(r'^mov-mensalista-novo/$', movmensalista_novo, name='core_movimento_mensalista_novo'),
    re_path(r'^mov-mensalista-update/(?P<id>\d+)\$', movmensalista_update, name='core_movimento_mensalista_update'),
    re_path(r'^mov-mensalista-delete/(?P<id>\d+)\$', movmensalista_delete, name='core_movimento_mensalisa_delete'),
]
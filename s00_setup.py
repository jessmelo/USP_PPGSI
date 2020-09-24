#!/usr/bin/env python
import networkx as nx
import numpy as np
import seaborn as sns
import matplotlib as plt
import os

from s01_load import *
from s02_plot import *
from s03_functions import *
from s04_metrics import *

print('')
print('#####################################################################')
print('## PPGSI - EACH/USP 2020 ############################################')
print('## LCDS  - 5965830       ############################################')
print('## Similaridades v2      ############################################')
print('#####################################################################')
print('')

arquivo = input('Deseja transformar um aquivo OWL/RDF em csv? 1-Sim/2-Não')
print(arquivo)
if arquivo == '1':
    importa_OWL_RDF()


print('---------------------------------------------------------------------')
print('* Ontologias disponíveis:')

dic=criar_menu_arq()

ontologia=input('Qual arquivo/ontologia você deseja utilizar?')
print(dic[int(ontologia)])

print('---------------------------------------------------------------------')
print('* Medidas de similaridade disponíveis: !!apenas sim_path até agora!!')
print('1 - Sim_path :  Caminho mínimo')
print('2 - Sim_wup  :  Wu e Palmer')
print('3 - Sim_lch  :  Leacock e Chodorow')
print('4 - Sim_nam  :  Nguyen e Al-Mubaid')
print('---------------------------------------------------------------------')

metrica = input('Escolha uma medida (utilize os números):')

metrica_dic={
    '1':'Sim_path',
    '2':'Sim_wup',
    '3':'Sim_lch',
}

print('')
print('* Seleção:')
print(dic[int(ontologia)]+' e '+ metrica_dic[metrica])
base=dic[int(ontologia)]

print('---------------------------------------------------------------------')

print('')
print('#####################################################################')
print('## Carga de dados ###################################################')
print('#####################################################################')
print('')

#ontologia
df=carga_de_onto_01(dic[int(ontologia)])

nos=nos(df)
arestas=arestas(df)

qtd_nos(df)
qtd_arestas(df)

print('')
print('#####################################################################')
print('## Construção do grafo - plot 01 ####################################')
print('#####################################################################')
print('')

grafo_imagem = input('Deseja representar a imagem do grafo? 1-Sim/2-Não')
print('* Escolha: '+str(grafo_imagem))
if grafo_imagem == '1':
    draw_grafo=draw_Digraph(nos,arestas,base)


print('')
print('#####################################################################')
print('## Calculo da similaridade ##########################################')
print('#####################################################################')
print('')

H=build_graph_nx(nos,arestas)
G=build_Digraph_nx(nos,arestas)

draw_tree(G, True)

print("Medida selecionada: "+ str(metrica_dic[metrica]))

if metrica_dic[metrica] == 'Sim_path':
    m=matriz_sim_path(H,nos,base)

elif metrica_dic[metrica] == 'Sim_wup':
    m=matriz_sim_wup(G, nos, base)

else:
    print("sem medida")

print('')
print('#####################################################################')
print('## Fim ##############################################################')
print('#####################################################################')
print('')
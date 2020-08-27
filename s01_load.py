from owlready2 import *
import pandas as pd
import os
#from os import walk

###################################################################
# Encontrar arquivos no diretório de dados

def encontrar_arq():
    path = './data/'
    for path, diretorios, arquivos in walk('./data/') :
        #print(arquivos)
        lista=arquivos
        #print(lista)
    return lista

###################################################################
# Criar menu de setup
'''
def criar_menu_arq():
    menu=encontrar_arq()

    menu_list = []
    n = 0
    for i in menu:
        print(n, i)
        menu_list.append((n,i))
        n = n + 1

    dic=dict(menu_list)
    #print(dict(menu_list))
    return dic
'''
def criar_menu_rdf():
    path = './data/'

    arr = os.listdir(path)

    lista = [arq for arq in arr if
             (arq.endswith(".owl") or (arq.endswith(".rdf")))]

    menu_list = []
    n = 0
    for i in lista:
        print(n, i)
        menu_list.append((n,i))
        n = n + 1

    dic=dict(menu_list)
    #print(dict(menu_list))
    return dic

def criar_menu_arq():
    path = './data/'

    arr = os.listdir(path)

    lista = [arq for arq in arr if
             (arq.endswith("_adj.csv"))]

    menu_list = []
    n = 0
    for i in lista:
        print(n, i)
        menu_list.append((n,i))
        n = n + 1

    dic=dict(menu_list)
    #print(dict(menu_list))
    return dic
###################################################################
# Processo de transformação dos arquivos

def importa_OWL_RDF():

    print('')
    print('Arquivos disponíveis para transformação:')
    print('')

    #Indicação de diretório e arquivo de entrada
    onto_path.append("./data/")

    dic=criar_menu_rdf()

    print('')
    arquivo = input('Qual arquivo deseja transformar?')
    nome=dic[int(arquivo)]
    print(nome)

    onto = get_ontology(nome).load()

    class root(Thing):
        namespace = onto

    #Apresentação das classes

    classes=list(onto.classes())

    lista=[]
    s=0
    for i in classes:
        s=s+1
        lista.append(i)
        #print(i)

    print('')
    print('************************************************')
    print('Quantidade de classes na ontologia: '+str(s))
    print('************************************************')
    #print('')

    '''
    s=0
    for i in classes:
        for u in list(onto.get_children_of(i)):
            #print(a)
            s = s + 1
            print(i.is_a,i,onto.get_children_of(i))
            #for t in onto.get_children_of(i):
             #   print(i, t)
    '''


    #print('Quantidade de subclasses na ontologia: '+str(s))
    #print('************************************************')
    #print('')

    #print('**************************')
    #print('**************************')

    x=[]
    s=0
    for i in classes:
        for u in list(onto.get_children_of(i)):
            #print(i.is_a[0],i)
            a=(i,i.is_a[0])
            x.append(a)
            s = s + 1

    #print(s)
    #print('**************************')
    #print('**************************')

    s=0
    for i in classes:
        for l in range(len(onto.get_children_of(i))):
            #print(i,'|',onto.get_children_of(i)[l])
            b=(onto.get_children_of(i)[l],i)
            x.append(b)
            s = s + 1
    #print(s)

    df=pd.DataFrame(x)
    df.columns=['n1','n2']

    df['prop']='is-a'
    df=df.drop_duplicates()

    df.to_csv('./data/'+str(dic[int(arquivo)])+'_adj.csv', index = False, sep='|')
    print('./data/'+str(dic[int(arquivo)])+'_adj.csv')
    print('')
    print(df.head(3))
    print('')
    print('Import ok!')
    print('************************************************')
    print('')
    return()

def carga_de_onto_01(base):
    print('./data/'+str(base))
    df=pd.read_csv('./data/'+str(base),decimal=".",delimiter='|')
    print(df.head(3))
    return df


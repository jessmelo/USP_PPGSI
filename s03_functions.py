import networkx as nx
import pandas as pd
import seaborn as sns
import matplotlib as plt

###################################################################
# Retorna os nós do grafo
def nos(df):
    nos = set(pd.concat([df['n1'], df['n2']]))
    nos=list(nos)
    return nos

###################################################################
# Apresenta a quantidade de nós do grafo
def qtd_nos(df):
    print('')
    qtd = set(pd.concat([df['n1'], df['n2']]))

    print('Quantidade de nós: '+str(len(qtd)))
    return qtd

###################################################################
# Retorna as arestas do grafo
def arestas(df):
    arestas = []
    for i in range(df.shape[0]):
        # a=(df.loc[i][0],df.loc[i][1],{'weight':df.loc[i][2]})
        a = (df.loc[i][0], df.loc[i][1], df.loc[i][2])
        arestas.append(a)
    return arestas

###################################################################
# Apresenta as arestas do grafo
def qtd_arestas(df):
    arestas = []
    for i in range(df.shape[0]):
        # a=(df.loc[i][0],df.loc[i][1],{'weight':df.loc[i][2]})
        a = (df.loc[i][0], df.loc[i][1], df.loc[i][2])
        arestas.append(a)

    qtd=len(arestas)
    print('Arestas: '+str(qtd) )

    return qtd

###################################################################
# Construção do grafo em networkx
def build_graph_nx(nos,arestas):
    G=nx.Graph()
    G.add_nodes_from(nos)
    G.add_weighted_edges_from(arestas)
    return G

###################################################################
# Construção do grafo orientado em networkx
def build_Digraph_nx(nos,arestas):
    G=nx.DiGraph()
    G.add_nodes_from(nos)
    G.add_weighted_edges_from(arestas)
    return G
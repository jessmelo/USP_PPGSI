import networkx as nx
import pandas as pd
import seaborn as sns
import matplotlib as plt

###################################################################
# Apresenta a menor distância entre os nós
def shortest_path_length(H,i,j):
    short_parth=nx.shortest_path_length(H,source=i,target=j)
    return(short_parth)

#Métrica de similaridade Spath
def sim_spath(H,i,j):
    try:
        res=1/shortest_path_length(H,i,j)
    except:
        res=0
    return(res)

#Métrica de similaridade Sim_wup

def sim_wup(G, i, j):
    # definindo o no raiz da arvore
    root = "owl.Thing"

    # calculando o Least Common Subsumer (Ancestor)
    LCS = nx.lowest_common_ancestor(G, i, j)

    H = G.to_undirected()
    # calculando a profundidade dos nos =  menor caminho do no até a raiz
    depth_lcs = sim_spath(H, root, LCS)
    depth_node1 = sim_spath(H, root, i)
    depth_node2 = sim_spath(H, root, j)

    try:
        sim_wup = (2 * depth_lcs) / (depth_node1 + depth_node2)
    except ZeroDivisionError:
        sim_wup = 0

    return(sim_wup)

'''
#Métrica de similaridade Sim_lch
def sim_lch(G, node1, node2):
    # medindo o menor caminho do grafo nao direcionado
    G_undirected = G.to_undirected()
    shortest_path = nx.shortest_path_length(G_undirected, node1, node2)

    # calcula profundidade do grafo
    Depth_ontology = nx.dag_longest_path_length(G)

    # formula:
    sim_lch = -math.log( shortest_path / (2 * Depth_ontology))

    return sim_lch
'''

#Matriz de similaridade
def matriz_sim_path(H,nos,base):
    #u=metrica
    #n = len(nos)
    m = []
    for i in nos:
        for j in nos:
            res = sim_spath(H, i, j)
            #print(i, j, round(res, 2))
            m.append([i, j, round(res, 2)])

    m = pd.DataFrame(m)
    m = m.pivot_table(2, 0, 1, fill_value=0)

    m = pd.DataFrame(m)
    m.to_csv('./data/out/'+'out_matrix_sim_path_'+str(base), index=True)
    print('Matriz de similaridades: '+'./data/out/' + 'out_matrix_sim_path_' + str(base))
    return(m)

#Matriz de similaridade
def matriz_sim_wup(G, nos, base):
    m = []
    for i in nos:
        for j in nos:
            res = sim_wup(G, i, j)

            #print(i, j, round(res, 2))
            m.append([i, j, round(res, 2)])

    m = pd.DataFrame(m)
    m = m.pivot_table(2, 0, 1, fill_value=0)

    m = pd.DataFrame(m)
    m.to_csv('./data/out/'+'out_matrix_sim_wup_'+str(base), index=True)
    print('Matriz de similaridades: '+'./data/out/' + 'out_matrix_sim_wup_' + str(base))

    return(m)
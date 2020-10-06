import networkx as nx
import pandas as pd
import seaborn as sns
import matplotlib as plt
import math

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
        res=1.0
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

#Métrica de similaridade Sim_lch
def sim_lch(G, i, j):
    # medindo o menor caminho do grafo nao direcionado
    G_undirected = G.to_undirected()
    shortest_path = sim_spath(G_undirected, i, j)

    # calcula profundidade do grafo
    Depth_ontology = nx.dag_longest_path_length(G)

    # formula:
    lch = shortest_path / (2 * Depth_ontology)
    if(lch == 0):
        sim_lch = 0
    else:
        sim_lch = -math.log(lch)
    return sim_lch

def information_content(G, node):
    # calcula information content de um nó
    descendants = nx.descendants(G, node)

    descendants_leaves = []
    for node in descendants:
        if (G.in_degree(node)!=0 and G.out_degree(node)==0):
            descendants_leaves.append(node)
    
    num_descendants_leaves = len(descendants_leaves)

    subsumers = nx.ancestors(G, node)
    num_subsumers = len(subsumers)

    leaf_nodes = [node for node in G.nodes() if G.in_degree(node)!=0 and G.out_degree(node)==0]
    max_leaves = len(leaf_nodes)

    calc = (num_descendants_leaves / num_subsumers + 1) / (max_leaves + 1)
    ic = -math.log(calc)
    return ic
    
#Métrica de Resnik
def sim_resnik(G, node1, node2):
    # Least Common Subsumer
    LCS = nx.lowest_common_ancestor(G, node1, node2)
    
    if(LCS == None):
        sim_res = 1.0
    else:
        # calcula information content do least common subsumer
        sim_res = information_content(G, LCS)
    return sim_res

def sim_lin(G, node1, node2):
    LCS = nx.lowest_common_ancestor(G, node1, node2)
    sim_lin = (2.0 * information_content(G, LCS)) / (information_content(G, node1) + information_content(G, node2))
    return sim_lin

#Matriz de similaridade sim_path
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

#Matriz de similaridade wup
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
    
#Matriz de similaridade lch
def matriz_sim_lch(G, nos, base):
    m = []
    for i in nos:
        for j in nos:
            res = sim_lch(G, i, j)

            #print(i, j, round(res, 2))
            m.append([i, j, round(res, 2)])

    m = pd.DataFrame(m)
    m = m.pivot_table(2, 0, 1, fill_value=0)

    m = pd.DataFrame(m)
    m.to_csv('./data/out/'+'out_matrix_sim_lch_'+str(base), index=True)
    print('Matriz de similaridades: '+'./data/out/' + 'out_matrix_sim_lch_' + str(base))

    return(m)

#Matriz de similaridade Resnik
def matriz_sim_resnik(G, nos, base):
    m = []
    for i in nos:
        for j in nos:
            res = sim_resnik(G, i, j)

            #print(i, j, round(res, 2))
            m.append([i, j, round(res, 2)])

    m = pd.DataFrame(m)
    m = m.pivot_table(2, 0, 1, fill_value=0)

    m = pd.DataFrame(m)
    m.to_csv('./data/out/'+'out_matrix_sim_resnik_'+str(base), index=True)
    print('Matriz de similaridades: '+'./data/out/' + 'out_matriz_sim_res' + str(base))

    return(m)
    
#Matriz de similaridade Lin
def matriz_sim_lin(G, nos, base):
    m = []
    for i in nos:
        for j in nos:
            res = sim_lin(G, i, j)

            #print(i, j, round(res, 2))
            m.append([i, j, round(res, 2)])

    m = pd.DataFrame(m)
    m = m.pivot_table(2, 0, 1, fill_value=0)

    m = pd.DataFrame(m)
    m.to_csv('./data/out/'+'out_matrix_sim_lch_'+str(base), index=True)
    print('Matriz de similaridades: '+'./data/out/' + 'out_matriz_sim_lin' + str(base))

    return(m)
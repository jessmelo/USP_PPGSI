import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.transforms as mtransforms
from matplotlib.transforms import Bbox
from graphviz import Digraph
from networkx.drawing.nx_pydot import graphviz_layout

# Plot de grafo
def draw_Digraph(nos,arestas,base):

    g = Digraph('G', filename='./data/out/'+'out_plot_'+str(base),format='pdf')
    g.attr(rankdir='RL', size='8,4', pad='3')
    #g.attr(rankdir='LR', size='8,4', nodesep='0.5', ranksep='1.25', pad='.5')

    #g.attr('node', shape='box', style='filled', fillcolor = 'lightgray')
    g.attr('node', shape='box', style='rounded,filled', fillcolor='lightgray')

    for i in nos:
        g.node(i)            

    for i in arestas:
        #print(i[0],i[1],i[2])
        g.edge(i[0],i[1], label=str(i[2]))

    g.view()
    print('Plot 01 - ok!')
    return g

def add_root_node(G):
    grafo = G
    for i in list(grafo.nodes): 
        ancestors = list(ancestors(G, i))
        if not ancestors:
            G.edge(i, "Thing", label="is-a")
    
    return G

def draw_tree(G, label):
    plt.title("Ontology")
    pos=graphviz_layout(G, prog='dot')
    nx.draw(G, pos, with_labels=label, arrows=False)
    plt.show()
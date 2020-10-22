from scipy import stats
from s04_metrics import *
import numpy as np
from numpy import genfromtxt

#Correlação de Spearman
def spearman(data1, data2):
    coef, p = stats.spearmanr(data1, data2, nan_policy='omit')
    alpha = 0.05
    print("Coeficiente de correlação: " + str(coef))
    if p > alpha:
	    print("Não há correlação entre os dados")
    else:
	    print("Correlação alta: p=" + str(p))

    return coef

AlsatianWine_spath = genfromtxt('./data/out/teste_wine_spath.csv', delimiter=';')
AlsatianWine_simwup = genfromtxt('./data/out/teste_wine_sim_wup.csv', delimiter=';')

# calcula a correlação entre a métrica Shortest Path e Wu&Palmer
correlation = spearman(AlsatianWine_spath, AlsatianWine_simwup)

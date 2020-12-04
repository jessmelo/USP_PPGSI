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
	    print("p=" + str(p))

    return coef

AlsatianWine_spath = genfromtxt('./data/out/teste_wine_spath.csv', delimiter=';')
AlsatianWine_simwup = genfromtxt('./data/out/teste_wine_sim_wup.csv', delimiter=';')
DessertCourse_spath = genfromtxt('./data/out/teste_wine_spath_dessert.csv', delimiter=';');
DessertCourse_simwup = genfromtxt('./data/out/teste_wine_sim_wup_dessert.csv', delimiter=';');
# calcula a correlação entre a métrica Shortest Path e Wu&Palmer

Wine_SimWup = genfromtxt('./data/out/out_matrix_sim_wup_wine_ontology_adj.csv', delimiter=',')
Wine_Spath = genfromtxt('./data/out/out_matrix_sim_spath_wine_ontology_adj.csv', delimiter=',')

print("Correção entre os scores de AlsatianWine na Sim_Wup e Shortest Path: ")
correlation = spearman(AlsatianWine_spath, AlsatianWine_simwup)
print("################################\n")
print("Correção entre os scores de AlsatianWine e DessertCourse na SPath: ")
correlation = spearman(AlsatianWine_spath, DessertCourse_spath)
print("################################\n")
print("Correção entre os scores de DessertCourse na Sim_Wup e Shortest Path: ")
correlation = spearman(DessertCourse_spath, DessertCourse_simwup)
print("################################\n")
print("Correção entre os scores da ontologia Wine na Sim_Wup e Shortest Path: ")
coef, p = stats.spearmanr(Wine_SimWup, Wine_Spath, axis=1, nan_policy='omit')
print(coef)

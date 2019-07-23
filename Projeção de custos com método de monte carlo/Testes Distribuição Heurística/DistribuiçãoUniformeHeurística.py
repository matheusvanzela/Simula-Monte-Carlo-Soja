# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:52:31 2019

@author: matheus vanzela

Algoritmo para geração de números aleatórios baseado no Método de Monte Carlo.
A estratégia de geração foi a distribuição uniforme uniforme.

"""
import pandas as pd
import numpy as np
import random
#import matplotlib.pyplot as plt
 
MatrizGerada=[]
rt=[]
#variável que armazena o número de cenários aleatórios a serem gerados
ncenários=10000
nmeses=12

#Leitura de dados do arquivo DadosDistTriangular
#df=pd.read_excel('DadosDistHeurística.xlsx',index_col='ano') (Indexando as colunas pela coluna 'ano')
df=pd.read_excel('DadosDistHeurística.xlsx','SojaCEPEA')
#elimina as células com valores nulos
df.dropna()
#atribui um dataframe apenas com as colunas correspondentes aos meses
dfmeses=df[['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']]
#recupera o valor mínimo, máximo, médio e o desvio padrão para cada um dos meses do dataframe.
MinMensal=dfmeses.min()
MaxMensal=dfmeses.max()
MedianaMensal=dfmeses.median()
AvgMensal=dfmeses.mean()
StdMensal=dfmeses.std()

#recuperando as somas anuais 
SomaAnual=[] #Não precisa desta declaração, serve apenas como controle de variáveis para este autor
for i in range(len(dfmeses)):
    SomaAnual.append((dfmeses.loc[i]).sum())

#Recuperando o menor valor do último ano da série histórica
MenorValorÚltimoAno=dfmeses.loc[len(dfmeses)-1].min()

#Recuperando o maior valor do último ano da série histórica
MaiorValorÚltimoAno=dfmeses.loc[len(dfmeses)-1].max()    

#contabilizando o cresimento ano a ano, sempre comparando o ano psosterior com o ano anterior
TaxaAnual=[]
for i in range(len(SomaAnual)):
    if i == 0:
        continue
    TaxaAnual.append(SomaAnual[i]/SomaAnual[i-1])

#recuperando a maior das taxas ano a ano calculadas e armazenadas em TaxaAnual
MaiorTaxaAnual=np.matrix(TaxaAnual).max()

#recuperando o crescimento médio para a série pesquisada
TaxaMédiaAnual=np.matrix(TaxaAnual).mean()
"""
Gerador de cenários baseado numa distribuição uniforme com uma heurística de atribuir:
ao valor mínimo: o menor valor do último ano da série histórica incrementado ao crescimento médio Ano a Ano
ao valor máximo: o maior valor observado no último ano da série histórica incrementado da maior taxa de crescimento Ano a Ano observada
"""
for j in range(nmeses):
    rt=[]
    for i in range(ncenários):
        rt.append(random.uniform(MenorValorÚltimoAno*TaxaMédiaAnual,MaiorValorÚltimoAno*MaiorTaxaAnual))
    MatrizGerada.append(rt)
    
MatrizGerada=np.matrix(MatrizGerada)
MatrizGerada=np.transpose(MatrizGerada)
MatrizGerada=pd.DataFrame(MatrizGerada,columns=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'])


#construção do vetor que soma todas as linhas da matriz de resultados
VarSoma=[]
for i in range(ncenários):
    var=[]
    var=(MatrizGerada.loc[i]).sum()
    VarSoma.append(var)

#inserção de uma nova coluna representando a soma na matriz de resultados
MatrizGerada['SOMA']=VarSoma


#rotina para escrever os resultados em uma planilha excel
ResumoEstatístico=MatrizGerada.describe()
mzfinal=MatrizGerada.append(ResumoEstatístico)
mzfinal.to_excel('ResultadosHeurística.xlsx')







    



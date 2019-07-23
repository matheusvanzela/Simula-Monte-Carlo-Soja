# -*- coding: utf-8 -*-
"""
Created on Fri Jul 19 13:52:31 2019

@author: matheus vanzela

Algoritmo para geração de números aleatórios baseado no Método de Monte Carlo.
A estratégia de geração foi a distribuição uniforme triangular.

"""
import pandas as pd
import numpy as np
import random

#Função para recuperar valores min, max e mediana do dataframe (não foi utilizada)
#def rec (Mes,MatrizArmazenamento):
#    #MatrizArmazenamento=
#    MatrizArmazenamento.append((min(Mes),max(Mes),np.median(Mes)))
#    MatrizArmazenamento=np.matrix(MatrizArmazenamento)
#    return MatrizArmazenamento
    
MatrizGerada=[]
rt=[]
obs=7
ncenários=1000
periodo=12

#Leitura de dados do arquivo DadosDistTriangular
df=pd.read_excel('DadosDistTriangular.xlsx','SojaCEPEA')
df.dropna()
dfmeses=df[['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']]
MinMensal=dfmeses.min()
MaxMensal=dfmeses.max()
MedianaMensal=dfmeses.median()

for j in range(ncenários):
    rt=[]
    for i in range(periodo):
        rt.append(random.triangular(MinMensal[i],MaxMensal[i],MedianaMensal[i]))
    MatrizGerada.append(rt)

MatrizGerada=np.matrix(MatrizGerada)
np.transpose(MatrizGerada)
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
#MatrizGerada=pd.DataFrame(MatrizGerada,columns=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'])
ResumoEstatístico=MatrizGerada.describe()
mzfinal=MatrizGerada.append(ResumoEstatístico)
mzfinal.to_excel('ResultadosTriangular.xlsx')

    



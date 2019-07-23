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
 
MatrizGerada=[]
rt=[]
obs=7
ncenários=1000
periodo=12

#Leitura de dados do arquivo DadosDistTriangular
df=pd.read_excel('DadosDistUniforme.xlsx','SojaCEPEA')
df.dropna()
dfmeses=df[['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']]
MinMensal=dfmeses.min()
MaxMensal=dfmeses.max()
MedianaMensal=dfmeses.median()

for j in range(ncenários):
    rt=[]
    for i in range(periodo):
        rt.append(random.uniform(MinMensal[i],MaxMensal[i]))
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
ResumoEstatístico=MatrizGerada.describe()
mzfinal=MatrizGerada.append(ResumoEstatístico)
mzfinal.to_excel('ResultadosUniforme.xlsx')




    



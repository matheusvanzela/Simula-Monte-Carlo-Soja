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
ncenários=1000

#Leitura de dados do arquivo DadosDistTriangular
df=pd.read_excel('DadosDistNormal.xlsx','SojaCEPEA')
df.dropna()
dfmeses=df[['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez']]
MinMensal=dfmeses.min()
MaxMensal=dfmeses.max()
MedianaMensal=dfmeses.median()
AvgMensal=dfmeses.mean()
StdMensal=dfmeses.std()

for i in range(ncenários):
    rt.append(random.normalvariate(AvgMensal,StdMensal))

#rotina par escrever os resultados em uma planilha excel
MatrizGerada=np.matrix(rt)
MatrizGerada=pd.DataFrame(MatrizGerada,columns=['jan','fev','mar','abr','mai','jun','jul','ago','set','out','nov','dez'])

#construção do vetor que soma todas as linhas da matriz de resultados
VarSoma=[]
for i in range(ncenários):
    var=[]
    var=(MatrizGerada.loc[i]).sum()
    VarSoma.append(var)

#inserção de uma nova coluna representando a soma na matriz de resultados
MatrizGerada['SOMA']=VarSoma

#recuperação de um resumo estatístico no final da matriz de resultados    
ResumoEstatístico=MatrizGerada.describe()
mzfinal=MatrizGerada.append(ResumoEstatístico)
#geração de um arquivo com os resultados compilados
mzfinal.to_excel('ResultadosNormal.xlsx')






    



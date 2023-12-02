# -*- coding: utf-8 -*-
"""
Created on Wed Nov 29 16:45:32 2023

@author: kamma
"""
import csv
import numpy as np

class HashTabel:
    def __init__(self): #Inicializar
        self.max = 6
        self.arr = [ [] for i in range(self.max)]
        
    def get_hash(self, key): #Fazer a função de hash baseado em divisão
        h = 0
        for char in key:
            h += ord(char)
        return h % self.max
    
    def __getitem__(self,key): # Acessar o data 
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if key == element[0]:
                return element[1] 

    
    def __setitem__(self, key, valor): #Mudar o data
        h = self.get_hash(key) 
        if len(self.arr[h]) == 0: #Olhar se não já foi usado aquele valor de hash
            self.arr[h].append((key,valor))
        
        found = False
        for index, element in enumerate(self.arr[h]): #Olhar se já tem essa "key"
            if key == element[0]:
                self.arr[h][index] = (key, valor)
                found = True
        if found == False:
            self.arr[h].append((key,valor)) #Se não tem, vamos criar e colocar um novo
        return
    
    def __delitem__(self, key): #Deletar um valor
        h = self.get_hash(key)
        for index, element in enumerate(self.arr[h]):
            if key == element[0]:
                del self.arr[h][index] 
           
        
    def load(self, data): #De uma lista de tuplas criar o hash tabela correspondente 
        for index in np.arange( len(data) ):
            key = data[index][0]
            valor = data[index][1]
            self[key] = valor
        return
    
    def destribution(self): #Para ter uma ideá se o data é bem distribuição 
        p = []
        for i in np.arange( len(self.arr) ):
            p.append(len(self.arr[i]))
        return p,np.var(p)
    
    
# Baixando a dada escolhido
weather = []
with open("nyc_weather.csv", "r") as f: 
    for line in f:
        print(line)
        tokens = line.split(",")
        date = tokens[0]
        temperature = float(tokens[1])
        weather.append((date,temperature))
    del weather[0]
    
s = HashTabel()
load(s, weather)

#Testar que as funções estão funcionando
s['Jan 9'] = 100.0 
print(s.arr)
del s['Jan 10']
print(s.arr)
p, var = destribution(s)
print(p,var)






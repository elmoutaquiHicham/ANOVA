import pandas as pd
import numpy as np

class ANOVA :
    def __init__(self, columns):
        self.columns = columns
        self.k = len(self.columns)
        
    def remplissez_dataframe(self): 
        df = pd.DataFrame(columns = self.columns)
        for i in range(len(self.columns)):
            print('donnez la série de données pour le traitement '+ str(i))
            lst = []
            n = int(input("Veuillez entrer le nombre d'élements  n"+str(i)))
            for j in range(0, n):
                ele = int(input())
                lst.append(ele)
            df[self.columns[i]] = lst
            lst = []
        global data 
        data = df
        display(df)
        
    def MU(self):
        V = 0
        C = 0
        for i in self.columns :
            C += len(data[i])*np.mean(data[i])
            V += len(data[i])
    
        return float(C/V)  
        
    def SCT(self):

        N=0
        for i in self.columns : 
            for j in range(len(data[i])):
                N += (data[i][j] - float(self.MU()))**2
        
        return float(N)
    
    def SCR(self):
        N=0
        for i in self.columns:
            for j in range(len(data[i])):
                N+= (data[i][j] - data[i].mean())**2
            
        return float(N)
    
    def SCTr(self):
        N = 0
        for i in self.columns : 
            for j in range(len(data[i])):
                N+= (np.mean(data[i]) - (self.MU()))**2
            
        return float(N)
    
    def n(self): 
        C = 0
        for i in data.columns : 
            C+= len(data[i])
        return int(C)
    
    def ANOVA_1F_fixe(self):
    

        df = pd.DataFrame( {'Somme des carrées (SC)': [self.SCTr(), self.SCR(), self.SCT()], 'Degrés de liberté (ddl)' : [self.k -1 , self.n() - self.k  , self.n() - 1] , 'Moyenne des carrées (MC)': [self.SCTr()/(self.k -1) , self.SCR()/(self.n()-self.k), '-----' ], 'F': [(self.SCTr()/(self.k -1)/(self.SCR()/(self.n()-self.k))), '------','------'] })
        indexes = ['Intergroupes (Traitement)', 'Intragroupe (Erreur)', 'Total']
        df.index = indexes
    
        display(df)
    
    
          

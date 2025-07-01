import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_car_vs_company(A,dict1,dict2):

    B=[]
    D=[]
    for x in A['Car']:
        C = str(x.split()[0])
        D.append(C)
    A['Company'] = D
    CName = A['Company'].value_counts()
    plt.barh(list(CName.index.values), CName.iloc[:])
    plt.subplots_adjust(bottom = 0.08,top = 0.99,left = 0.11)
    plt.xlabel('Number of Car Models Released from 1970-82',fontdict = dict1)
    plt.ylabel('Car Companies',fontdict = dict2)
    for i, v in enumerate(CName.iloc[:]):
        plt.text(v, i , str(v),
        color = 'blue', fontweight = 'bold')
        
    plt.tight_layout()
    plt.show()

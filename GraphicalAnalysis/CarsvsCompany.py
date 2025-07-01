import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def get_car_vs_company():
    B=[]
    D=[]
    for x in A['Car']:
        C = str(x.split()[0])
        D.append(C)
    A['Company'] = D
    CName = A['Company'].value_counts()

    F = A['Model'].value_counts()
    Year = A['Model'].unique()
    plt.barh(list(CName.index.values), CName.iloc[:])
    plt.subplots_adjust(bottom = 0.08,top = 0.99,left = 0.11)
    plt.xlabel('Number of Car Models Released from 1970-82',fontdict = dict1)
    plt.ylabel('Car Companies',fontdict = dict2)
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    for i, v in enumerate(CName.iloc[:]):
        plt.text(v, i , str(v),
        color = 'blue', fontweight = 'bold')
    plt.show()

import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


def get_car_vs_origin():
    A = pd.read_csv('cars.csv' , sep = ';' , skiprows = [1] )
    C = []
    Country = A['Origin'].unique()
    for x in Country :
        B = len(A[A['Origin'] == x ])
        C.append(B)
    plt.pie(C,labels =Country,autopct='%1.1f%%',shadow = True,explode = [0,0,0.2],colors = ['#6495ED','#FFD700','r'])
    plt.legend()
    plt.title('Percentage of Cars made in diffrent regions during 1970 -82 ',fontdict = dict2,loc = 'center' ) 
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    plt.show()
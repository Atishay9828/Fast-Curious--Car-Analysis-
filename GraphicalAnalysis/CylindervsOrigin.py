import pandas as pd
import matplotlib.pyplot as plt


def get_cylinder_vs_origin(A,dict1,dict2):

    C = []
    D = []

    Country = A['Origin'].unique()
    Cylinders = A['Cylinders'].unique()
    US = []
    EU = []
    JA = []

    for x in Country :
        B = len(A[ A['Origin'] == x ])
        C.append(B)
                        
    for x in Cylinders :
        B = len(A[ A['Cylinders'] == x ])
        D.append(B)

    for x in Cylinders :
        B = len(A[(A['Cylinders'] == x) & (A['Origin'] == Country[0])])
        US.append(B)
        
    for x in Cylinders :
        B = len(A[(A['Cylinders'] == x) & (A['Origin'] == Country[1])])
        EU.append(B)
        
    for x in Cylinders :
        B = len(A[(A['Cylinders'] == x) & (A['Origin'] == Country[2])])
        JA.append(B)    

    plt.subplot(3,1,1)
    plt.bar(Cylinders , US, label = 'US',color = 'm',linestyle = '-.',linewidth = 1,edgecolor = 'k')
    plt.xlabel('Number of Cylinders',fontdict = dict1)
    plt.ylabel('Quantity Made',fontdict = dict2)
    plt.grid(color = 'k',linestyle = (0, (3, 10, 1, 10)))
    plt.legend(['US'])

    plt.subplot(3,1,2)
    plt.bar(Cylinders , EU ,label = 'Europe',color = 'b',linestyle = '-.',linewidth = 1,edgecolor = 'k')
    plt.xlabel('Number of Cylinders',fontdict = dict1)
    plt.ylabel('Quantity Made',fontdict = dict2)
    plt.grid(color = 'k',linestyle = (0, (3, 10, 1, 10)))
    plt.legend(['Europe'],loc = 'upper left')

    plt.subplot(3,1,3)
    plt.subplots_adjust(bottom = 0.11,top = 0.95,wspace = 0.37,hspace = 0.51)
    plt.bar(Cylinders , JA , label = 'Japan',color = 'k',linestyle = '-.',linewidth = 1,edgecolor = 'k')
    plt.xlabel('Number of Cylinders',fontdict = dict1)
    plt.ylabel('Quantity Made',fontdict = dict2)
    plt.grid(color = 'k',linestyle = (0, (3, 10, 1, 10)))
    plt.legend(['Japan'],loc = 'upper left')


    plt.tight_layout()
    plt.show()
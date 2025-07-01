import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def get_hp_vs_mpg(A,dict1,dict2):

    df = pd.DataFrame(A)
    df['MPG'] = df['MPG'].astype(float)
    df['Horsepower'] = df['Horsepower'].astype(float)
    sns.relplot(x = 'Horsepower',
                    y = 'MPG',data = A,size = 'Cylinders', kind = 'scatter',hue = 'Cylinders');
    plt.xlabel('Horsepower',fontdict = dict1)
    plt.ylabel('MPG',fontdict = dict1)
    plt.grid(color = 'k',linestyle = '--')
    plt.title('Comparison between Horsepower and MPG of different cars of various Cylinders',
                    fontdict = dict2,loc = 'center')
    plt.subplots_adjust(top = 0.94)
    
    plt.tight_layout()
    plt.show()
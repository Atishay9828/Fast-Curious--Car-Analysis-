import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def get_hp_vs_mpg():
    A = pd.read_csv('cars.csv', sep = ';', skiprows = [1])
    b = []
    d = []
    for x in A['Car']:
        b.append(x)
    c = len(b)
    for x in b:
        c = str(x.split()[0])
        d.append(c)
    A['Company'] = d
    CName = A['Company'].unique()
    df = pd.DataFrame(A)
    df['MPG'] = df['MPG'].astype(float)
    df['Cylinders'] = df['Cylinders'].astype(float)
    df['Displacement'] = df['Displacement'].astype(float)
    df['Horsepower'] = df['Horsepower'].astype(float)
    df['Weight'] = df['Weight'].astype(float)
    df['Acceleration'] = df['Acceleration'].astype(float)
    df['Model'] = df['Model'].astype(float)
    df.dtypes
    sns.relplot(x = 'Horsepower',
                    y = 'MPG',data = A,size = 'Cylinders', kind = 'scatter',hue = 'Cylinders');
    plt.xlabel('Horsepower',fontdict = dict1)
    plt.ylabel('MPG',fontdict = dict1)
    plt.grid(color = 'k',linestyle = '--')
    plt.title('Comparison between Horsepower and MPG of different cars of various Cylinders',
                    fontdict = dict2,loc = 'center')
    plt.subplots_adjust(top = 0.94)
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')

    plt.show()
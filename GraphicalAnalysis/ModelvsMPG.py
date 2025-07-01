import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def get_model_vs_mpg():
    A = pd.read_csv('cars.csv', sep = ';', skiprows = [1])
    b = []
    d = []
    for x in A['Car']:
        b.append(x)
    c = len(b)
    #print(c)
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
    sns.relplot(x="Model", y="MPG", data=A, kind="line", errorbar='sd',style="Origin", hue="Origin");
    plt.xlabel('Model',fontdict = dict1)
    plt.ylabel('MPG',fontdict = dict1)
    plt.grid(color = 'k',linestyle = '--')
    plt.title('Comparison between Model and MPG of different cars of various origins',
                fontdict = dict2,loc = 'center')
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    plt.show()
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_weight_vs_displacement():
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
    sns.relplot(x = 'Weight',
                y = 'Displacement',data = A,style = 'Origin', kind = 'scatter',hue = 'Origin');
    plt.xlabel('Weight',fontdict = dict1)
    plt.ylabel('Displacement(in Miles)',fontdict = dict1)
    plt.grid(color = 'k',linestyle = '--')
    plt.title('Comparison between Weight and Displacement of different cars of various origins',
                fontdict = dict2,loc = 'center')
    plt.subplots_adjust(top= 0.94)
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    plt.show()

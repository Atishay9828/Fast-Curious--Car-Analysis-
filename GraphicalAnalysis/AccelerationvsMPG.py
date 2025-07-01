import pandas as pd ,matplotlib.pyplot as plt,numpy as np,seaborn as sns

def get_acc_vs_mpg() :
        
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
    sns.relplot(x = 'Acceleration',
    y = 'MPG',data = A,style = 'Origin', kind = 'scatter',hue = 'Origin');
    plt.xlabel('Acceleration',fontdict = dict1)
    plt.ylabel('MPG',fontdict = dict1)
    plt.grid(color = 'k',linestyle = '--')
    plt.title('Comparison between Acceleration and MPG of different cars of various origins',
    fontdict = dict2,loc = 'center')
    plt.subplots_adjust(top = 0.95)
    manager = plt.get_current_fig_manager()
    manager.window.state('zoomed')
    plt.show()

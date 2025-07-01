import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


def get_weight_vs_displacement(A,dict1,dict2):

    df = pd.DataFrame(A)
    df['Displacement'] = df['Displacement'].astype(float)
    df['Weight'] = df['Weight'].astype(float)
    sns.relplot(x = 'Weight',
                y = 'Displacement',data = A,style = 'Origin', kind = 'scatter',hue = 'Origin');
    plt.xlabel('Weight',fontdict = dict1)
    plt.ylabel('Displacement(in Miles)',fontdict = dict1)
    plt.grid(color = 'k',linestyle = '--')
    plt.title('Comparison between Weight and Displacement of different cars of various origins',
                fontdict = dict2,loc = 'center')
    plt.subplots_adjust(top= 0.94)
    
    plt.tight_layout()
    plt.show()

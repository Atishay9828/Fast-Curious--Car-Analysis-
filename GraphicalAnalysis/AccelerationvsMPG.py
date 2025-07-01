import pandas as pd 
import matplotlib.pyplot as plt
import seaborn as sns

def get_acc_vs_mpg(A,dict1,dict2) :

    df = pd.DataFrame(A)
    
    df['MPG'] = df['MPG'].astype(float)
    df['Acceleration'] = df['Acceleration'].astype(float)
    sns.relplot(x = 'Acceleration',
    y = 'MPG',data = A,style = 'Origin', kind = 'scatter',hue = 'Origin')
    plt.xlabel('Acceleration',fontdict = dict1)
    plt.ylabel('MPG',fontdict = dict1)
    plt.grid(color = 'k',linestyle = '--')
    plt.title('Comparison between Acceleration and MPG of different cars of various origins',
    fontdict = dict2,loc = 'center')
    plt.subplots_adjust(top = 0.95)

    plt.tight_layout()
    plt.show()

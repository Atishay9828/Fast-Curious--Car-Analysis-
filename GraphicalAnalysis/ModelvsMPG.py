import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def get_model_vs_mpg(A,dict1,dict2):
  
    df = pd.DataFrame(A)
    df['MPG'] = df['MPG'].astype(float)
    df['Model'] = df['Model'].astype(float)
    df.dtypes
    sns.relplot(x="Model", y="MPG", data=A, kind="line", errorbar='sd',style="Origin", hue="Origin");
    plt.xlabel('Model',fontdict = dict1)
    plt.ylabel('MPG',fontdict = dict1)
    plt.grid(color = 'k',linestyle = '--')
    plt.title('Comparison between Model and MPG of different cars of various origins',
                fontdict = dict2,loc = 'center')
    
    plt.tight_layout()
    plt.show()
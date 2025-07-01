import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import seaborn as sns


def get_model_vs_hp(A,dict1,dict2):

    df = pd.DataFrame(A)

    df['Horsepower'] = df['Horsepower'].astype(float)
    df['Model'] = df['Model'].astype(float)
    sns.relplot(x=df["Model"], y=df["Horsepower"], 
                data=df, kind="line", style="Origin", hue="Origin",
                    dashes=False)
    plt.xlabel('Model',fontdict = dict1)
    plt.ylabel('Horsepower',fontdict = dict1)
    plt.grid(color = 'k',linestyle = '--')
    plt.title('Comparison between Model and Horsepower of different cars of various origins',
                fontdict = dict2,loc = 'center')
    plt.legend()

    plt.tight_layout()
    plt.show()
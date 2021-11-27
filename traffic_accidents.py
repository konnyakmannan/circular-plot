import matplotlib
from matplotlib import pyplot as plt
import numpy as np
import pandas as pd

plt.rcParams['xtick.major.pad'] = '17'
plt.rcParams["axes.axisbelow"] = False
plt.rcParams['font.size'] =  17
matplotlib.rc('axes',edgecolor='w')

import re

def read_data() -> pd.DataFrame:
    try:
        df_orig = pd.read_csv(
        './data/traffic-accidents-kanagawa-reiwa2.tsv',
         sep='\t', header=0, index_col=0,
         )
    except BaseException as e:
        print(e)
    else:
        df = df_orig.applymap(
                lambda x: x.replace(',', '')
            ).applymap(
                lambda x: re.compile(r'\d+').findall(x)[0]
            ).astype(int)
    return df
    
def main():
    df = read_data()
    df['theta'] = np.linspace(0.0, 2.0*np.pi, df.shape[0], endpoint=False)

    average = df['12月'].mean()

    fig, ax = plt.subplots(figsize=(15, 15), subplot_kw={'projection': 'polar'})
    ax.bar(
        df.theta, df['12月'], alpha=0.5, width=0.5,
        label='事故発生件数'
         )
    ax.plot(
        np.linspace(0, 2*np.pi, 256), average * np.ones(256), 
        color='red', linestyle='--', label='時間帯平均'
        )
    ax.set_title('令和２年12月中の時間帯別交通事故発生件数', fontname='Cica')
    ax.set_xticks(df.theta)
    ax.set_xticklabels([f'{i}-{i+2}' for i in range(0, 24, 2)])
    ax.set_yticks([100, 200, 300, 400])
    ax.legend(prop={'family':'Cica'}, loc='center')
    plt.savefig('./image/traffic-accidents-kanagawa-reiwa2.png')
    plt.show();

        
if __name__=='__main__':
    main()

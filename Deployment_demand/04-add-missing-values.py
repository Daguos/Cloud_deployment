# 04-add-missing-values.py
import numpy as np
import pandas as pd
from datetime import datetime, timedelta

if __name__ == "__main__":
    
    df = pd.read_csv("./data/timeseries.csv")

    df['dteday'] = df['dteday'].astype('datetime64[ns]')

    for i in range(0,17379):
        df['dteday'][i] = df.dteday[i] + timedelta(hours=df['hr'].tolist()[i])

    df_new_cope = df.copy()

    df_new_cope = (df_new_cope.set_index('dteday')
        .reindex(pd.date_range("20110101 0000", "20121231 2300", freq='1H')
        .strftime('%Y%m%d %H%M')))
    df_new_cope.reset_index(inplace=True)
    df_new_cope.columns = df.columns
    df_new_cope['dteday'] = df_new_cope['instant']
    updated_df = df_new_cope.astype({'dteday':'datetime64[ns]'})
    updated_df = pd.DataFrame(updated_df['dteday'])

    df = pd.merge_asof(updated_df, df, on='dteday')

    hr_ = []
    for i in range(0,24):
        hr_.append(i)
    df["hr"] = hr_*731

    def rightRotate(lists, num): 
        output_list = [] 
        
        # Will add values from n to the new list 
        for item in range(len(lists) - num, len(lists)): 
            output_list.append(lists[item]) 
            
        # Will add the values before 
        # n to the end of new list     
        for item in range(0, len(lists) - num):  
            output_list.append(lists[item]) 
            
        return output_list

    days_ = []
    for i in range(0,7):
        days_.append(i)
    days_ = np.sort(days_*24)
    days_ = rightRotate(days_,24)
    days_ = days_*105
    df["weekday"] = days_[:17544]

    df.to_csv('./data/timeseries-no-missing.csv')
    
    print('Complete')
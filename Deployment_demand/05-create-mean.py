#05-create-mean
import pandas as pd
import numpy as np


if __name__ == "__main__":
    df = pd.read_csv("./data/timeseries-no-missing.csv")

    df = df.reset_index()
    df['weeks_mean'] = np.nan
    for i in range(0,169):
        df['weeks_mean'][i] = 0
    for i in range(168,336):
        df['weeks_mean'][i] = df['cnt'][i-168]
    for i in range(336,504):
        df['weeks_mean'][i] = np.round(np.mean([df['cnt'][i-168],df['cnt'][i-336]]))
    for i in range(504,len(df)):
        df['weeks_mean'][i] = np.round(np.mean([df['cnt'][i-168],df['cnt'][i-336],df['cnt'][i-504]]))

    df.to_csv('./data/timeseriesWithMean.csv')

    print('Completed')
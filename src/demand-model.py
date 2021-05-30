import pickle
import numpy as np
import pandas as pd
from sklearn.metrics import accuracy_score
from sklearn.ensemble import RandomForestRegressor
from sklearn.preprocessing import MinMaxScaler
from sklearn.pipeline import Pipeline



if __name__ == "__main__":

    #Datasets: Prep    
    datos = pd.read_csv('./data/timeseriesWithMean.csv')

    feature_columns = ["yr", "mnth","hr","season", "holiday","weekday","workingday", "weathersit","temp","atemp", "hum","windspeed","cnt","weeks_mean"]
    target_column = "cnt"
    y_new = datos[target_column]
    X_new = datos[feature_columns]

    ind_new = datos["yr"] == 0
    X_train_n, y_train_n = X_new[ind_new], y_new[ind_new]
    X_test_n, y_test_n = X_new[~ind_new], y_new[~ind_new]

    assert X_new.shape[0] == X_train_n.shape[0] + X_test_n.shape[0]

    col = ["hr","season", "holiday","weekday","weeks_mean"]
    x_trainf = X_train_n[col]
    x_testf = X_test_n[col]

    #model trianing 
    pipe_rf = Pipeline(steps=[("scaler", MinMaxScaler()),
        ("rfmodel", RandomForestRegressor(n_estimators=16, max_depth=10))
    ])

    pipe_rf.fit(x_trainf, y_train_n)

    #Predictions
    predictions=pipe_rf.predict(x_testf)
    print(pipe_rf.predict([[13,1,1,5,209.0]]))
    
    #Registro
    with open('./outputs/demand_model.pkl', 'wb') as model_pkl:
        pickle.dump(pipe_rf, model_pkl)
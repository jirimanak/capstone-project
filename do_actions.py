
import pandas as pd
import numpy as np

from sklearn.preprocessing import LabelEncoder

def encode_categorical_column(data, column):
    label_encoder = LabelEncoder()
    label_encoder.fit(data[column])
    data[column] = label_encoder.transform(data[column])
    return data

def encode_categorical(data, categoricaldata):

    for column in categoricaldata:
        data = encode_categorical_column(data, column)

    return data


def remove_this_Ids(df, toremove):
    if isinstance(toremove, list):
        for o in toremove:
            df = df[df.Id != o]
        else:
            df = df[df.Id != o]
    return df


# Adding total sqfootage feature
def add_TotalSF(data):
    data['TotalSF'] = data['TotalBsmtSF'] + data['1stFlrSF'] + data['2ndFlrSF'] + data['GarageArea']
    return data

def add_TotalSF_log(data):
    data['TotalSF_log'] = np.log(data['TotalBsmtSF'] + data['1stFlrSF'] + data['2ndFlrSF'])
    return data


def unskew(data, col_name):
    data[col_name] = np.log1p(data[col_name])
    return data

def unskew_columns(data, columns):
    for col in columns:
        data = do_unskew(data, col)
    return data


def remove_outliers_simple(data):
    data = data.drop(data[(data['GrLivArea']>4000) & (data['SalePrice']<300000)].index)
    return data
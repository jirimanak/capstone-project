import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import platform

def load_data():
    # Load the Boston housing dataset
    if platform.system() == 'Windows':
        data_train = pd.read_csv('data\\train.csv')
        data_test = pd.read_csv('data\\test.csv')
    else:
        data_train = pd.read_csv('data/train.csv')
        data_test = pd.read_csv('data/test.csv')
    return data_train, data_test



def plot_distro(data_train, data_name):
    plot_data = data_train[data_name]
    plot_data_log = plot_data.apply(np.log)

    plt.figure(figsize=(20,5))
    ax = plt.subplot(1,2,1)
    ax.axvline(plot_data.mean(),linewidth=1, color='b')
    ax.axvline(plot_data.median(),linewidth=1, color='r')
    sns.distplot(plot_data, bins=50)
    plt.title('Original Data')
    plt.xlabel(data_name)

    ax = plt.subplot(1,2,2)
    sns.distplot(plot_data_log, bins=50)
    ax.axvline(plot_data_log.mean(),linewidth=1, color='b')
    ax.axvline(plot_data_log.median(),linewidth=1, color='r')
    plt.title('Natural Log of Data')
    plt.xlabel('Natural Log of {}'.format(data_name))
    plt.tight_layout()

    print("           Skewness: {0:0.4f}   Kurtosis: {1:0.4f}".format(plot_data.skew(), plot_data.kurt()))
    print("Log scale  Skewness: {0:0.4f}   Kurtosis: {1:0.4f}".format(plot_data_log.skew(), plot_data_log.kurt()))

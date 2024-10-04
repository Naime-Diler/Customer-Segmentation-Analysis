# K-Means Unsupervised Learning for Segmentation 


# Importing Necessary Libraries
import warnings
warnings.simplefilter(action='ignore', category=FutureWarning)

import numpy as np
import pandas as pd
import seaborn as sns
from matplotlib import pyplot as plt
# !pip install missingno
import missingno as msno
from sklearn.model_selection import train_test_split
from sklearn.preprocessing import MinMaxScaler, LabelEncoder, StandardScaler, RobustScaler
from sklearn.cluster import KMeans
from scipy.cluster.hierarchy import dendrogram
from scipy.cluster.hierarchy import linkage
from yellowbrick.cluster import KElbowVisualizer
from sklearn.cluster import AgglomerativeClustering


# Reading Datasets
df = pd.read_csv("data/Mall_Customers.csv")
df1 = df.copy()


def grab_col_names(dataframe, cat_th=10, car_th=20):
    """

    Listet die Namen der kategorischen, numerischen und kardinalen Variablen im Datensatz auf.
    Hinweis: Zu den kategorischen Variablen zählen auch numerisch erscheinende, kategorische Variablen.

    Parameters
    ------
        dataframe: dataframe
                Der DataFrame, aus dem die Variablennamen extrahiert werden sollen.
        cat_th: int, optional
                Schwellenwert für die Klassen von numerischen, aber kategorischen Variablen.
        car_th: int, optinal
                Schwellenwert für die Klassen von kategorischen, aber kardinalen Variablen.

    Returns
    ------
        cat_cols: list
                Liste der kategorischen Variablen.
        num_cols: list
                Liste der numerischen Variablen.
        cat_but_car: list
                Liste der kategorisch erscheinenden kardinalen Variablen.

    Examples
    ------
        import seaborn as sns
        df = sns.load_dataset("iris")
        print(grab_col_names(df))


    Notes
    ------
        num_but_cat befindet sich innerhalb von cat_cols.
        Die Summe der drei Listen, die zurückgegeben werden, entspricht der Gesamtzahl der Variablen:
        cat_cols + num_cols + cat_but_car = Anzahl der Variablen.

    """

    # cat_cols, cat_but_car
    cat_cols = [col for col in dataframe.columns if dataframe[col].dtypes == "O"]
    num_but_cat = [col for col in dataframe.columns if dataframe[col].nunique() < cat_th and
                   dataframe[col].dtypes != "O"]
    cat_but_car = [col for col in dataframe.columns if dataframe[col].nunique() > car_th and
                   dataframe[col].dtypes == "O"]
    cat_cols = cat_cols + num_but_cat
    cat_cols = [col for col in cat_cols if col not in cat_but_car]

    # num_cols
    num_cols = [col for col in dataframe.columns if dataframe[col].dtypes != "O"]
    num_cols = [col for col in num_cols if col not in num_but_cat]

    print(f"Observations: {dataframe.shape[0]}")
    print(f"Variables: {dataframe.shape[1]}")
    print(f'cat_cols: {len(cat_cols)}')
    print(f'num_cols: {len(num_cols)}')
    print(f'cat_but_car: {len(cat_but_car)}')
    print(f'num_but_cat: {len(num_but_cat)}')
    return cat_cols, num_cols, cat_but_car

cat_cols, num_cols, cat_but_car = grab_col_names(df1)

# Data_Preparation

# Encoding
binary_cols = [col for col in df1.columns if df1[col].dtype not in [int, float]
               and df1[col].nunique() == 2]

def label_encoder(dataframe, binary_col):
    labelencoder = LabelEncoder()
    dataframe[binary_col] = labelencoder.fit_transform(dataframe[binary_col])
    return dataframe


for col in binary_cols:
    df1 = label_encoder(df1, col)

df1.head()

# Scaling
scaler = RobustScaler()
df1[num_cols] = scaler.fit_transform(df1[num_cols])

df1[num_cols].head()



# Determine the optimum number of clusters.
kmeans = KMeans()
elbow = KElbowVisualizer(kmeans, k=(2, 20))
elbow.fit(df1)
elbow.show(block=True)

elbow.elbow_value_



# Create your model and segment your customers.
k_means = KMeans(n_clusters = 6, random_state= 42).fit(df1)
segments=k_means.labels_
segments


df["segment"] = segments
df.head()
df.columns

df.groupby("segment").agg({"Annual Income (k$)":["mean","count"]})

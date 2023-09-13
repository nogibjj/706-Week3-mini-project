import matplotlib.pyplot as plt
import polars as pl
import pandas as pd


def polars_describe(polars_data):
    return polars_data.describe()


def get_median(polars_data):
    return polars_data.median()


def PlotShapeLeng(csv):
    pd.set_option("display.max_columns", None)
    polars_data = pl.read_csv(csv)
    plt.figure(figsize=(10, 6))
    plt.hist(polars_data["Shape_Leng"], bins=20, edgecolor="black")
    plt.title("Shape_Leng Distribution")
    plt.xlabel("Shape_Leng")
    plt.ylabel("Count")
    plt.show()

def PlotShapeArea(csv):
    pd.set_option("display.max_columns", None)
    polars_data = pl.read_csv(csv)
    plt.figure(figsize=(10, 6))
    plt.hist(polars_data["Shape_Area"], bins=20, edgecolor="black")
    plt.title("Shape_Area Distribution")
    plt.xlabel("Shape_Area")
    plt.ylabel("Count")
    plt.show() 

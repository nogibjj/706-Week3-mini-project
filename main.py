import pandas as pd
import matplotlib.pyplot as plt
from ydata_profiling import ProfileReport
import polars as pl


def polars_describe(csv):
    polars_data = pl.read_csv(csv)
    return polars_df.describe()


def get_median(csv):
    polars_data = pl.read_csv(csv)
    return polars_df.median()


def PlotShapeLeng(csv):
    pd.set_option("display.max_columns", None)
    polars_data = pl.read_csv(csv)
    plt.figure(figsize=(10, 6))
    plt.hist(general_df["Shape_Leng"], bins=20, edgecolor="black")
    plt.title("Shape_Leng Distribution")
    plt.xlabel("Shape_Leng")
    plt.ylabel("Count")
    plt.show()

def PlotShapeArea(csv):
    pd.set_option("display.max_columns", None)
    polars_data = pl.read_csv(csv)
    plt.figure(figsize=(10, 6))
    plt.hist(general_df["Shape_Area"], bins=20, edgecolor="black")
    plt.title("Shape_Area Distribution")
    plt.xlabel("Shape_Area")
    plt.ylabel("Count")
    plt.show() 

def polars_summary(csv):
    polars_data = pl.scan_csv(csv)
    profile = ProfileReport(polars_data, title="Profiling Report")
    profile.to_file("polars.html")

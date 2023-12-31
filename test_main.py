from main import (
    polars_describe,
    get_median,
    PlotShapeLeng,
    PlotShapeArea,
)
import polars as pl

example_csv = "https://catalogue.data.wa.gov.au/dataset/f39087e2-2885-473e-bc62-ca610cd94340/resource/96c892f3-b387-410c-80d0-e4dcec68e6f2/download/25ktopomapseriesindex.csv"

def test_descirbe():
    data = pl.read_csv(example_csv)
    result = polars_describe(data)
    assert result[["describe", "Shape_Area"]][2, 1] == 228153453.41946846
    assert result[["describe", "Shape_Leng"]][2, 1] == 60622.470193439854
    assert result[["describe", "Shape_Area"]][3, 1] == 7611513.495851165
    assert result[["describe", "Shape_Leng"]][3, 1] == 1094.0062261219582

def test_median():
    data = pl.read_csv(example_csv)
    assert get_median(data['Shape_Leng']) == 60896.5746
    assert get_median(data['Shape_Area']) == 230060526.252

def test_plot1():
    PlotShapeLeng(example_csv)

def test_plot2():
    PlotShapeArea(example_csv)

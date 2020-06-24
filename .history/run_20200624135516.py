import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import sklearn.linear_model


# Loading the data
oecd_bli = pd.read_csv("oced_bli_2015.csv", thousands=",")
gdp_per_capita = pd.read_csv(
    "oced_bli_2015.csv", thousands=",", delimiter="\t", encoding="latin1", na_values="n/a")

country_stat = prepare_country_stats(oecd_bli, gdp_per_capita)

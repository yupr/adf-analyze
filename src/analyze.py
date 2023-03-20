#! /usr/bin/env python

# run script
# poetry run python src/analyze.py

import pandas as pd
from statsmodels.tsa.stattools import adfuller
import matplotlib.pyplot as plt

beforeData = pd.read_csv("dataSets/before.csv")
afterData = pd.read_csv("dataSets/after.csv")

beforeData["date"] = pd.to_datetime(beforeData["date"])
afterData["date"] = pd.to_datetime(afterData["date"])

# 指定した列をindexに割り当て、昇順にソート
beforeData = beforeData.set_index(["date"]).sort_index(ascending=True)
afterData = afterData.set_index(["date"]).sort_index(ascending=True)

# ADF検定
def checkAdf(fileName: str, data: pd.DataFrame):
    # 原系列のp値を算出 (p値 == 単位根過程の確率)
    adf = adfuller(data)[1]

    print(fileName, "のP値:", adf)
    if adf <= 0.05:
        print("帰無仮説が棄却され、定常性があると言える。\n")
    else:
        print("単位根過程であるため、非定常性であると言える。\n")


# 増減率の算出
def calcRateOfChange(before: pd.DataFrame, after: pd.DataFrame, column: str):
    # 平均
    beforeAverage = before[column].mean()
    afterAverage = after[column].mean()

    rateOfChange = (afterAverage - beforeAverage) / beforeAverage * 100
    print("増減率:", rateOfChange, "%")


checkAdf("before", beforeData["count"])
checkAdf("after", afterData["count"])
calcRateOfChange(beforeData, afterData, "count")

beforeData.plot()
afterData.plot()

plt.show()

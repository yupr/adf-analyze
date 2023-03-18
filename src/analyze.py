#! /usr/bin/env python

# run script
# poetry run python src/analyze.py

import pandas as pd
import statsmodels.api as sm
import matplotlib.pyplot as plt

before = pd.read_csv("dataSets/before.csv")
after = pd.read_csv("dataSets/after.csv")

before["date"] = pd.to_datetime(before["date"])
after["date"] = pd.to_datetime(after["date"])

# 指定した列をindexに割り当て、昇順にソート
before = before.set_index(["date"]).sort_index(ascending=True)
after = after.set_index(["date"]).sort_index(ascending=True)

# ADF検定で定常性を確認 ---------------------
def checkAdf(fileName, data):
    adf = sm.tsa.stattools.adfuller(data)[1]

    print(fileName, "のP値:", adf)
    if adf <= 0.05:
        print("帰無仮説が棄却され、定常性があると言える。")
    else:
        print("単位根過程であるため、非定常性であると言える。")
    print("---------------------------------")


# 原系列のp値を算出 (単位根過程の確率)
checkAdf("before", before["count"])
checkAdf("before", after["count"])
# ------------------------------------------

before.plot()
after.plot()

plt.show()

#! /usr/bin/env python
# script: poetry run python src/practice.py

# 2020年12月のカレンダーを表示 ------------------------------------
# import calendar
# print(calendar.prmonth(2020, 12))


# 独自関数 -----------------------------------------------------------
# ももとみかんの個数から合計金額を計算する関数
# def fruit_price(peachCount, mikanCount):
#     totalPrice = (peachCount * 100) + (mikanCount * 40)
#     return totalPrice

# isInputCorrect = False

# while isInputCorrect == False:

#     peachCount = input("桃の個数を入力してください。")
#     mikanCount = input("みかんの個数を入力してください。")

#     if peachCount.isdecimal() & mikanCount.isdecimal():
#         peachCount = int(peachCount)
#         mikanCount = int(mikanCount)
#         total = fruit_price(peachCount, mikanCount)
#         print("桃:", peachCount, "個", "みかん:", mikanCount, "個")
#         print("合計金額:", total, "円")
#         isInputCorrect = True
#     else:
#         print("\n-----------------------------------------------")
#         print("一方または両方の入力値が正しくないため、再度ご入力ください。")
#         print("------------------------------------------------\n")
#         continue


# for --------------------------------------------------------------------
# cases = [100, 125, 110, 135, 93, 95, 93]
# caseCount = 0

# for case in cases:
#     caseCount += case

# print("合計値part2:", caseCount)
# ------------------------------------------------------------------------


# キーワード引数 ---------------------------------------------------------
# def keywardArg(arg1, arg2, arg3="default3"):
#     print(arg1, arg2, arg3)
# keywardArg("arg1", arg2="arg2")
# ----------------------------------------------------------------------


# list object (jsだと配列に当たる) ----------------------------------------
# stations = ["東京", "品川", "新横浜", "小田原", "熱海"]

# # add: stationsの末尾に小岩を追加
# stations.insert(5, "小岩")
# print(stations)

# # remove 品川を削除
# del stations[1]
# print(stations)
# -----------------------------------------------------------------------


# 辞書オブジェクト ----------------------------------------------------------
# en_words = {"apple": "りんご", "orange": "みかん", "peach": "もも"}
# print("appleを日本語にすると:", en_words["apple"])

## 要素を追加
# en_words["banana"] = "ばなな"

## 要素を削除
# del en_words["banana"]
# print("remove banana:", en_words)

## count obj length
# print(len(en_words))


## in
# 入力した文字列が辞書オブジェクトに登録されいたら、対応する日本語を出力。
# 登録されていなければ、"登録されていません" と出力
# english_words = {"apple": "りんご", "orange": "みかん", "peach": "もも"}

# key = input("フルーツを英語で入力してください。")

# if key in english_words:
#     print("対応する日本語:", english_words[key])
# else:
#     print("登録されていません。")
# ------------------------------------------------------------------------


# tuple ------------------------------------------------------------------
## リストとの違い。データの追加と削除ができない。(更新することは可能)
# ningyochoPosition = (35.686321, 139.782211)
# print(ningyochoPosition)
# ------------------------------------------------------------------------


# スイカ割りゲーム
import random
import math

BOARD_SIZE = 5

# 初期位置を設定
def initialPosition(size):
    x = random.randrange(0, size)
    y = random.randrange(0, size)
    return (x, y)


# 2点間の距離を算出
def getDistance(position1, position2):
    diffX = position1[0] - position2[0]
    diffY = position1[1] - position2[1]
    distance = math.sqrt(diffX**2 + diffY**2)
    return distance


# 入力値に基づいてプレイヤーを移動
def movePosition(direction, position):
    positionX, positionY = position

    if direction == "n":
        positionY += 1
    elif direction == "s":
        positionY -= 1
    elif direction == "e":
        positionX += 1
    elif direction == "w":
        positionX -= 1

    return (positionX, positionY)


def suikaWari():
    suikaPosition = initialPosition(BOARD_SIZE)
    playerPosition = initialPosition(BOARD_SIZE)

    while suikaPosition != playerPosition:
        print("\n--------------------------------------------------------")
        print("Hint: スイカからプレイヤーまでの距離", getDistance(suikaPosition, playerPosition))
        print("--------------------------------------------------------\n")

        print("移動したい位置を入力してください。")
        direction = input("北の場合:n\n南の場合:s\n東の場合:e\n西の場合:w\n")
        currentPosition = movePosition(direction, playerPosition)
        playerPosition = currentPosition

    print("\n--------------------------------------------------------")
    print("ゲーム終了")
    print("--------------------------------------------------------")


suikaWari()

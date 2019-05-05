# -*- coding: utf-8 -*-
# ---
# jupyter:
#   jupytext:
#     text_representation:
#       extension: .py
#       format_name: light
#       format_version: '1.4'
#       jupytext_version: 1.1.1
#   kernelspec:
#     display_name: Python 3
#     language: python
#     name: python3
# ---

# # 分類
# ## 実際のデータを見てみる

from sklearn.datasets import load_breast_cancer

# +
breast_cancer = load_breast_cancer()
#特徴量
X = breast_cancer.data
#目的変数
y = breast_cancer.target

# 特徴量名
feature_names = breast_cancer.feature_names

## 英語で特徴量名が格納されている
## 10個よりおおくの特徴量がありそう
print(feature_names)

## "mean"が平均
## "error"が標準誤差
## "worst"が値が大きい３つの細胞の平均値を意味する

# Xのすべての行と10列目までを取り出す
X = X[:,:10]

# +
## 日本語の特徵量名の用意
columns = ['半径','テクスチャ','周囲の長さ','面積','なめらかさ','コンパクト性','へこみ','へこみの数','対称性','フラクタル次元']

## x,y,columnsを利用してデータフレームを作ってみる
from pandas import DataFrame
df = DataFrame(data=X[:, :10], columns=columns)
df['目的変数'] = y

##　下から５行を表示する
df.tail()
## 目的変数は 0は悪性　1は良性を意味する

# -


## 統計値をみてみる
df.describe()
## このデータには569個のサンプルが有り(count)の行　各特徴量の平均や再使用や最大値などをかんたんに求めることができる

# ## データをプロットしてデータの分布を確認してみる
# ### このデータは10次元のデータになっているから平面上(2次元)にぷろっとすることができません
# そこで１０個の特徴量から２個の特徴量を選んでそれぞれの組み合わせで平面にプロットする
#

# +
from matplotlib import pyplot
pyplot.rcParams['font.family'] = 'IPAPGothic'
from pandas.plotting import scatter_matrix

## 悪性の腫瘍を赤色、良性の腫瘍を青色にする
colors = ['red' if v == 0 else 'blue' for v in y ]

## 散布図の描画
axes = scatter_matrix(df[columns], figsize=(20,20), diagonal='kde', c = colors)
# -

#  ## このようにデータをプロットした図を散布図という
#  上図では青色が良性　赤色が悪性の腫瘍をしめしている
#
#  横軸が半径、縦軸が周囲の長さや面積の図をみてみるとデータがそれぞれ直線、放射線状に分布している様子がわかる
#  赤色と青色のデータをあるルールでなんとなく分離できそうな印象をもつ
#  
#  今回の講座では良性悪性判定を　面積　と　へこみ　の２つの特徴量を利用してといていく
#  
#  ## 実際のシステムを作り始める前にデータの分布を確認してしっかり方針を立てることが大事




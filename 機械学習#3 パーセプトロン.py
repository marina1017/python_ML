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

# # パーセプトロン
# ## パーセプトロンの概要
# 人工知能の分野においてニューロンの神経ネットワークを模倣した計算モデルをニューラルネットワークと呼ぶ
# パーセプトロンは　現在のニューラルネットワークやディープラーニングの基礎となっている理論です
#
# パーセプトロンは　y= {0,1}を識別する2値分類器
# たとえば腫瘍の良性を１　悪性１を０とするような問題をとける
# ![IMG_1050.PNG](attachment:IMG_1050.PNG)

# 図１は一つのニューロン　黒の実線はニューロンの結合を表している。
# ニューラルネットワークは複数のにゅーろんどうしのけつごうで　表現される。
# パーセプトロンは二層のニューラルネットワークで構成される
#
# 例
# 腫瘍データの場合　x1に細胞の半径　x2に細胞の面積と威風に特徴量が一つづつ入力される
#
# 入力層に入力された入力ｘが中間層で重みwとかけられた総和zが出力層に入力される
#
# ![IMG_1051.PNG](attachment:IMG_1051.PNG)

# ## パーセプトロンの学習
# 入力に対して適切な出力をするような重みwを適切に求めることが大事
#
# 過去の事例から良性または悪性となるような重みを求めることが目的
# **学習とは訓練データをうまく分類する重みwをもとめることである**
#
# ![IMG_1052.PNG](attachment:IMG_1052.PNG)

# +
## パーセプトロンの実験

### データの準備
from pandas import DataFrame
from sklearn.datasets import load_breast_cancer

breast_cancer = load_breast_cancer()
#特徴量
X = breast_cancer.data
#目的変数
y = breast_cancer.target

## 日本語の特徵量名の用意
columns = ['半径','テクスチャ','周囲の長さ','面積','なめらかさ','コンパクト性','へこみ','へこみの数','対称性','フラクタル次元']

## x,y,columnsを利用してデータフレームを作ってみる
from pandas import DataFrame
df = DataFrame(data=X[:, :10], columns=columns)
df['目的変数'] = y

## 特徴量として面積とへこみのみを利用するのでDataFrameからとりだします
x = df[['面積','へこみ']].values
y = df['目的変数'].values

# +
## 次にロードしたデータを訓練データとテストデータに分割する
### これは学習したモデルの性能評価をするための操作　 7割を訓練に　３割をテスト用のデータに分割する 訓練用に分割したデータを訓練データ　テスト用に分割したデータをテストセットと呼ぶ
### この操作にはscikit-learnのtrain_test_split()関数を使える
from sklearn.model_selection import train_test_split

### 訓練データをX_train, y_train テストデータを　x＿test, y_testという変数に代入する
### random_stateパラメータに分割方法のシードを与え再現性のある分割方法にした
X_train, X_test, y_train, y_test = train_test_split(X,y, test_size = 0.30, random_state=42)

print('すべてのデータ数=',len(y))
print('訓練データ数=',len(y_train))
print('テストデータ数=',len(y_test))

##　ちゃんと30%分割できていることがわかる
# -

# ## データの前処理
# 一般的に機械学習アルゴリズムに入力する特徴量のスケールをあわせておくのがよい
# ここでは標準化と呼ばれる操作をする
# 標準化はj番目の特徴量の平均をμｊ、標準偏差をσ
# $$
#     x_j = \frac{x_j - μ_j}{σ_j}
# $$
# の変換のことで平均が0　標準偏差が１となるように変換される
#
# 標準化の前処理は scikit-learnのStandardScalerに実装されているからそれを使うと良い
#

# +
##標準化の前処理は scikit-learnのStandardScalerに実装されているからそれを使うと良い
from sklearn.preprocessing import StandardScaler

## StandardScalerをimport後標準化に必要な平均と標準偏差を訓練データから求める
## StandardScalerのインスタンスを作成する
sc = StandardScaler()
## 訓練データの平均と標準偏差を計算する
sc.fit(X_train)

# -

## 求めた平均を確認してみます
print(sc.mean_)

# +
## 特徴量米に平均を計算しているため値が２こあります
## このscを利用して訓練データとテストデータを標準化します　transform()メソッドを利用する

## 訓練データの標準化
X_train_std = sc.transform(X_train)

## テストデータの標準化
## テストデータは訓練データの平均と標準偏差を用いて変換する
X_test_std = sc.transform(X_test)

## ここで、テストデータの変換には訓練データの平均と標準偏差が利用されている　同じscインスタンスを利用していることに注意する
## これはテストデータは未知であるという前提のためテストデータに施せるしょｒは既知のデータの情報のみで行われる必要があるから

# +
## 標準化後の訓練データの平均値
train_mean = X_train_std.mean(axis=0)
print(train_mean)

## 標準化後の訓練データの標準偏差
train_std = X_train_std.std(axis=0)
print(train_std )

## 壁んちがほぼ０分散が１になっているのが確認できる

# +
## 標準化後のテストデータの平均値
test_mean = X_test_std.mean(axis=0)
print(test_mean)

## 標準化後のテストデータの標準偏差
test_std = X_test_std.std(axis=0)
print(test_std)

## 訓練データほどの制度で平均０　標準偏差が１になってない
## テストデータと訓練データは一般的に異なるからこれが正常

# +
#　学習
## パーセプトロンの学習
from sklearn.linear_model import Perceptron

## Perceptionのインスタすを作成する
### max_iterは重みの最大更新回数　random_stateはら数生成シード値を固定するパラメーター　これにより実行のたびに結果が変わってしまうことを防ぐ
ppn = Perceptron(max_iter=1000, random_state=42)

### パーセプトロンを学習する　fit()メソッドを呼ぶだけ これだけで学習がおわる
ppn.fit(X_train_std, y_train)

# +
#予測
## 学習したパーセプトロンモデルを利用して未知のデータに対して予測を行ってみる
## predict()メソッドにテスト用のデータをわたす

## テストデータの予測
pred = ppn.predict(X_test_std)
print(pred)

## これは予測している
# -

## テストデータの正解値
print(y_test)

#　評価
## 予測値がどの程度正解しているかみてみる
## 正解率の計算もscikit-learnにおまかせする　accuracy_score()換羽雨を利用して正解率を求めてみる
from sklearn.metrics import accuracy_score
accuracy_score(y_test,pred)

# +
# 決定領域
## パーセプトロンが学習した決定領域を確認してみる
## 決定領域をプロットすることでパーセプトロンが最終的にどうやって学習したのか視覚的にわかるようにする

import numpy
from matplotlib import pyplot
pyplot.rcParams['font.family'] = 'IPAPGothic'
from mlxtend.plotting import plot_decision_regions

## すべてのデータをプロットするとデータが多すぎるので制限する
N = 100

## 訓練データとテストデータからN個ずつのサンプルを先頭からとってくる
sampled_X = numpy.vstack((X_train_std[:N], X_test_std[:N]))
sampled_Y = numpy.hstack((y_train[:N],y_test[:N]))
print(sampled_X )
print('/////////')
print(sampled_Y )

# +
## 上記コードでプロットするためのデータを用意　plot_decision_regions()関数にこれらのデータをいれる
pyplot.figure(figsize=(12,12))
pyplot.xlabel("面積")
pyplot.ylabel("へこみ")
pyplot.title("パーセプトロンの決定領域")

## 決定領域のプロット
plot_decision_regions(sampled_X, sampled_Y, clf=ppn, legend =2, X_highlight=X_test_std[:N])

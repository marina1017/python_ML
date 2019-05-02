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

1+1


# +
## テスト
### テスト


# -

squares = [1,2,4,51,43]
print(squares)


contacts = {'Taro':1234,'Jiro':5678}
print(contacts)
print(contacts['Taro'])
contacts['Saburo'] = 9012
print(contacts)

squares = [v** 2 for v in range(10)]
print(squares)

# +
import numpy
    
a = numpy.array([0,1,2,3])
print(a)

b = numpy.array([[0,1,2,3],[0,1,2,3]])
print(b)

print("a.shape",a.shape)
print("b.shape",b.shape)

print("a.shape",a.size)
print("b.shape",b.size)
# -

# # こんにちは
# ## あ
# #### あああ

# 0から４までの整数を持つ配列をつくる
print(numpy.arange(5))

# +
# 1から９までの整数のうち奇数の配列を作る
print(numpy.arange(1,10,3))

print("6", numpy.arange(6))
print("2*3",numpy.arange(6).reshape(2,3))

print(numpy.eye(2))


# -

# %matplotlib inline
from matplotlib import pyplot
pyplot.rcParams['font.family'] = 'IPAPGothic'

# +
import numpy
x = numpy.linspace(-numpy.pi * 2, numpy.pi *2 ,1024, endpoint=True)
y_sin = numpy.sin(x)
y_cos = numpy.cos(x)


#グラフサイズの変更
pyplot.figure(figsize=(11,7))
## 判例をつけるときはLabelを最後の引数に入れる必要がある
pyplot.plot(x, y_sin, color= 'blue', linewidth=3.0, label=r'$\sins(x)$')
pyplot.plot(x, y_cos, color= 'red', linewidth=1.0, label=r'$\co(x)$')

#x軸の最小値、最大値を xの最小値、最大値の1.2倍とする
pyplot.xlim(x.min() * 1.2, x.max()*1.2)
#y軸の最小値、最大値を y_sinの最小値、最大値の1.2倍とする
pyplot.xlim(y_sin.min() * 1.2, y_sin.max()*1.2)

# x軸のメモリ設定　リストを与える
pyplot.xticks([-numpy.pi * 2, -numpy.pi,0,numpy.pi,numpy.pi*2])
# y軸のメモリ設定　リストを与える
pyplot.yticks([-1, -0.5,0, 0.5,1])


# 判例追加
pyplot.legend()
# グラフ描画
pyplot.show()


# -
# # pandas
#


# +
import numpy
numpy.random.seed(42)
import pandas

# 10行５列の配列をつくる
data = numpy.random.randn(10,5)
print(data)

df = pandas.DataFrame(data, columns=['A','B','C','D','E'])
df

## 先頭３行を取得する
df.head(3)

## 後ろから３行をしゅとく
df.tail(3)

## index属性はDataFrameの行インデックス
df.index
### RangeIndex(start=0, stop=10, step=1)

## カラム名の取得
df.columns
### Index(['A', 'B', 'C', 'D', 'E'], dtype='object')

## DataFrameのデータ部分の取得
df.values
## array([[ 0.49671415, -0.1382643 ,  0.64768854,  1.52302986, -0.23415337],
#        [-0.23413696,  1.57921282,  0.76743473, -0.46947439,  0.54256004],
#        [-0.46341769, -0.46572975,  0.24196227, -1.91328024, -1.72491783],
#        [-0.56228753, -1.01283112,  0.31424733, -0.90802408, -1.4123037 ],
#        [ 1.46564877, -0.2257763 ,  0.0675282 , -1.42474819, -0.54438272],
#        [ 0.11092259, -1.15099358,  0.37569802, -0.60063869, -0.29169375],
#        [-0.60170661,  1.85227818, -0.01349722, -1.05771093,  0.82254491],
#        [-1.22084365,  0.2088636 , -1.95967012, -1.32818605,  0.19686124],
#        [ 0.73846658,  0.17136828, -0.11564828, -0.3011037 , -1.47852199],
#        [-0.71984421, -0.46063877,  1.05712223,  0.34361829, -1.76304016]])

### describe()メソッドは統計情報　最大値　最小値　平均などを計算してくる関数
df.describe()


df['B']


# 統計操作
## mean()メソッド
df.mean()

# %matplotlib inline
df.plot()
# -



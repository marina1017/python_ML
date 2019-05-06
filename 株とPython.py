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

# ## PyQueryの使い方

# +
from pyquery import PyQuery

q = PyQuery('https://kabutan.jp/stock/?code=7203')
sector = q.find('#stockinfo_i2 > div > a')[0].text
print(sector)
# -

# # Seleniumの使い方
# javaScriptで動的にページ内容を生成しているサイトではHTMLファイルからデータを取得できない
#

# +
from selenium import webdriver

## Firefoxはなんかうまくいかない
#driver = webdriver.Firefox('/usr/local/bin/geckodriver')
## とりあえずクロームで
driver = webdriver.Chrome('/usr/local/bin/chromedriver')
driver.get('http://jp.kabumap.com/servlets/kabumap/Action?SRC=basic/top/base&codetext=7203')
unit = driver.find_element_by_css_selector('#minUnit').text
print(unit)
## やったとれた！！

# +
from pyquery import PyQuery
import time
import sqlite3


def get_brand(code):
  url = 'https://kabutan.jp/stock/?code={}'.format(code)

  q = PyQuery(url)

  if len(q.find('div.company_block')) == 0:
    return None

  try:
    name = q.find('div.company_block > h3').text()
    code_short_name =  q.find('#stockinfo_i1 > div.si_i1_1 > h2').text()
    short_name = code_short_name[code_short_name.find(" ") + 1:]
    market = q.find('span.market').text()
    unit_str = q.find('#kobetsu_left > table:nth-child(4) > tbody > tr:nth-child(6) > td').text()
    unit = int(unit_str.split()[0].replace(',', ''))
    sector = q.find('#stockinfo_i2 > div > a').text()
  except (ValueError, IndexError):
    return None

  return code, name, short_name, market, unit, sector

def brands_generator(code_range):
  print("test",code_range)
  for code in code_range:
    print("code",code)
    print("get_brand(code)",get_brand(code))
    brand = get_brand(code)
    if brand:
      print("brand",brand)
      yield brand
    #time.sleep(1)

users = [
    ('1', 'name', 'shortname', 'market', 'java', 1),
    ('2', 'name', 'shortname', 'market', 'java', 1),
    ]

def insert_brands_to_db(db_file_name, code_range):
    print("brands_generator(code_range)",brands_generator(code_range))
  #conn = sqlite3.connect(db_file_name)
  #with conn:
    #sql = 'INSERT INTO brands(code,name,short_name,market,unit,sector) ' \'VALUES(?,?,?,?,?,?)'

    #print(users)
    #print(conn)
    #conn.executemany(sql, brands_generator(code_range))
    #conn.executemany(sql, users)
    
    conn = sqlite3.connect('brands')
    #c = conn.cursor()
    
    #sql = 'INSERT INTO brands(code,name,short_name,market,unit,sector) ' 
    conn.executemany("insert into brands values (?,?,?,?,?,?)" , brands_generator(code_range))
    conn.commit()
    conn.close()

## 実行
insert_brands_to_db('brand', range(1301,1303))

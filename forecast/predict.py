# AIを使った希少予測
import os
import numpy as np
import pandas as pd
from datetime import datetime as dt
from datetime import timedelta

#日付を季節に変換
def date2season(month, day):
    month, day = int(month), int(day)
    
    #データが範囲内であるかを確認
    if not (1 <= month <= 12 and 1 <= day <= 31):
        return 4 # 不正な日付
    
    #月を確認 - 1, 2季節ごとに判定
    if month == 2: #春,冬
        if day >= 4:
            return 0 #春
        elif day < 4:
            return 3 #冬
    elif month in [3, 4]: #春
        return 0 #春
    elif month == 5: #春,夏
        if day >= 5:
            return 1 #夏
        elif day < 5:
            return 0 #春
    elif month in [6, 7]: #夏
        return 1 #夏
    elif month == 8: #夏,秋
        if day >= 8:
            return 2 #秋
        elif day < 8:
            return 1 #夏
    elif month in [9, 10]: #秋
        return 2 #秋
    elif month == 11: #秋,冬
        if day >= 7:
            return 3 #冬
        elif day < 7:
            return 2 #秋
    elif month in [12, 1]: #冬
        return 3
    else:
        return 4 #エラー
    
# 数字を二桁に変換
def add_zero_to_single_digit(number):
    if 0 <= int(number) < 10:
        result = f'0{number}'
    else:
        result = str(number)
    
    return result

#CSVを読み込む
def load_csv(input_csv):
    #CSVを読み込む
    data = pd.read_csv(input_csv, dtype={'column_name': str}, low_memory=False)

    #CSVから日付を0埋め
    added_zero_dates = []
    for date in data['年月日時'].values.tolist():
        date_parts = date.split('/')
        year = int(date_parts[0])
        month = int(add_zero_to_single_digit(date_parts[1]))
        day = int(add_zero_to_single_digit(date_parts[2]))
        hour = int(add_zero_to_single_digit(date_parts[3]))

        added_zero_dates.append({'年': year, '月': month, '日': day, '時': hour})

    #結合
    df_added_zero = pd.DataFrame(added_zero_dates)
    data_2 = pd.concat([data, df_added_zero], axis=1)

    print(data_2)

#特徴量を抽出
def drop_feautures(input_data):
    #必要な列のみを抽出
    feautures = input_data.drop(['年月日時', '気圧_現地', '気圧_海面'], axis=1)

    #ターゲットを抽出
    target = feautures['気圧_現地' , '気圧_海面']

    return target

#欠陥値を調べる
def find_defective_value(input_data):
    return input_data.isnull().sum()


#抽出したものからトレーニングデータ作成

#トレーニング

#画像生成

#メイン
load_csv('test.csv')
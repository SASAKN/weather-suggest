import glob
import os

import numpy as np
import xarray as xr
from tqdm import tqdm

# 入力ベースパス
nc_base_path = "./surf_jra55"

# 出力ベースパス
np_base_path = "./surf_data_np"

# 目的のファイルを探す
def find_target_nc_file(year):
    result = glob.glob(f'{nc_base_path}/merged_{year}.nc')
    return result

# パスからデータセットを開く
def from_path_to_datasets(path_array):
    datasets = []
    for path in path_array:
        datasets.append(xr.open_dataset(path))
    return datasets

# NetCDF4をNumpyに変換
def nc2np(dataset, part):
    # part = トレーニングデータかテストデータか
    # dataset = データセットのデータ

    # ディレクトリを作成
    if part == "train":
        os.makedirs("./surf_data_np/train/", exist_ok=True)
    elif part == "test":
        os.makedirs("./surf_data_np/test", exist_ok=True)
    else:
        print(f'[ ERROR ! ]Unknown part : {part}')
        return
    
    
    


    

    


if __name__ == "__main__":

    # メッセージを表示
    print("Copyright SASAKEN 2024")


    # 年ごとに気象変数と時間を処理する
    for year in tqdm(range(1958, 2019), desc='Processing ...'):
        # データセットを読み込む
        datasets = from_path_to_datasets(find_target_nc_file(year))

        for dataset in datasets:

            # Numpy配列に変換する
            nc2np(dataset, "train")

        
    
            







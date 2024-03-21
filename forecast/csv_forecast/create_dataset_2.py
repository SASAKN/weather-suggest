import numpy as np
import pandas as pd

def fix_cloudiness(row_idx, col_idx, target_array):
    index = 0

    while True:
        if (col_idx - index) >= 0 and (col_idx + index) < target_array.shape[1]: 
            if index == 0 and target_array[row_idx, col_idx, 2] <= 10:
                break
            elif index != 0 and target_array[row_idx, (col_idx - index), 2] <= 10 and target_array[row_idx, (col_idx + index), 2] <= 10:  # 改変が必要である場合
                target_array[row_idx, col_idx, 2] = (target_array[row_idx, (col_idx - index), 2] + target_array[row_idx, (col_idx + index), 2]) / 2
                break

        index += 1

    result_array = target_array[row_idx, col_idx, 2]
    return result_array




if __name__ == "__main__":
    array = np.load('./npz_data/dataset.npz')['dataset']
    
    # STEP 1 雲量の補完

    #11以上は外れ値なので修正
    print('雲量(Cloud)を修正します。')
    outliner_cloud_index = np.argwhere(array[:, :, 2] > 10)
    outliner_cloud_array = array[outliner_cloud_index[:, 0], outliner_cloud_index[:, 1], 2]

    #外れ値を修正
    for outliner_cloud_idx in outliner_cloud_index:
        row_idx, col_idx = outliner_cloud_idx[0], outliner_cloud_idx[1]
        fix_cloudiness(row_idx, col_idx, array)
        print(array[row_idx, col_idx, 2])
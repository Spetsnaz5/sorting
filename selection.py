"""
插入排序演算法的運作如下：
    1.在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    2.從剩餘未排序元素中繼續尋找最小（大）元素，然後放到已排序序列的末尾。
    3.重複步驟1~2，直到所有元素均排序完畢。
"""

import random
# 隨機資料
data = [random.randint(10, 100) for _ in range(20)]

print(data)

def sort_steps(arr):
    n = len(arr)
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        
    return arr

sort = sort_steps(data.copy())

print(sort)
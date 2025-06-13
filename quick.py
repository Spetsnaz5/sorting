"""
快速排序演算法的運作如下：
    1.挑選基準值：從數列中挑出一個元素，稱為「基準」（pivot），
    2.分割：重新排序數列，所有比基準值小的元素擺放在基準前面，所有比基準值大的元素擺在基準後面（與基準值相等的數可以到任何一邊）。在這個分割結束之後，對基準值的排序就已經完成，
    3.遞迴排序子序列：遞迴地將小於基準值元素的子序列和大於基準值元素的子序列排序。
"""

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 建立隨機資料
data = [random.randint(10, 100) for _ in range(20)]

def quick_sort(arr):
    if len(arr) <= 1:
        return arr
    
    pointer = 0 # 替換元素索引
    pivot = len(arr) - 1 # 取最後一筆索引當基準
    
    for i in range(len(arr)):
        if arr[i] < arr[pivot]:
            arr[pointer], arr[i] = arr[i], arr[pointer]
            pointer += 1
            
    arr[pointer], arr[pivot] = arr[pivot], arr[pointer]
    
    left = quick_sort(arr[0:pointer]) # 比基準小
    right = quick_sort(arr[pointer + 1:len(arr)]) # 比基準大
    
    return left + [arr[pointer]] + right

# 執行排序
sort = quick_sort(data.copy())

print(data)
print(sort)
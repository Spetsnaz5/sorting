"""
合併排序演算法的運作如下：
    1.分割（Divide）：將資料不斷地對半切分，直到每一個子陣列只剩下一個元素為止。
    2.合併（Conquer）：將兩個有序子陣列合併成一個有序的陣列，逐層向上合併，直到回到原始陣列
"""
import random

# 產生隨機資料
data = [random.randint(10, 100) for _ in range(20)]

def merge_sort(arr):
    # 如果陣列長度小於等於 1，表示已經是「排序好」的狀態，直接回傳
    if len(arr) <= 1:
        return arr

    # 將陣列從中間切成左右兩半
    mid = len(arr) // 2
    left_half = merge_sort(arr[:mid])   # 對左半部遞迴做 merge sort
    right_half = merge_sort(arr[mid:])  # 對右半部遞迴做 merge sort

    # 合併左右兩個已經排序好的子陣列
    return merge(left_half, right_half)

def merge(left, right):
    result = []
    i = j = 0  # i 為左陣列指標，j 為右陣列指標

    # 用兩個指標比大小，把小的那個放進結果陣列
    while i < len(left) and j < len(right):
        if left[i] <= right[j]: 
            result.append(left[i])
            i += 1 # 小的放進陣列，且繼續i直到換j
        else:
            result.append(right[j])
            j += 1

    # 剩下的元素全部加進結果（只有一邊還有東西）
    result.extend(left[i:])
    result.extend(right[j:])
    
    return result

sorted = merge_sort(data)

print(data)
print(sorted)
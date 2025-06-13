"""
插入排序演算法的運作如下：
    1.從第一個元素開始，該元素可以認為已經被排序
    2.取出下一個元素，在已經排序的元素序列中從後向前掃描
    3.如果該元素（已排序）大於新元素，將該元素移到下一位置
    4.重複步驟3，直到找到已排序的元素小於或者等於新元素的位置
    5.將新元素插入到該位置後
    6.重複步驟2~5
"""
import random

data = [random.randint(10, 100) for _ in range(20)]

print(data)

def sort_steps(data):
    arr = data.copy()

    for i in range(1, len(arr)):
        key = arr[i]
        j = i - 1
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1
        
        arr[j + 1] = key

    return arr

# 預先執行排序並記錄所有動畫步驟
sort = sort_steps(data)

print(sort)

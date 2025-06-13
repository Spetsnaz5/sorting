"""
泡沫排序演算法的運作如下：
    比較相鄰的元素。如果第一個比第二個大，就交換它們兩個。
    對每一對相鄰元素作同樣的工作，從開始第一對到結尾的最後一對。這步做完後，最後的元素會是最大的數。
    針對所有的元素重複以上的步驟，除了最後一個。
    持續每次對越來越少的元素重複上面的步驟，直到沒有任何一對數字需要比較。
"""
import random

# 建立要排序的資料
data = [random.randint(10, 100) for _ in range(20)]

print(data)

def sort_steps(data):
    arr = data.copy()
    
    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
    
    return arr

steps = sort_steps(data)

print(steps)
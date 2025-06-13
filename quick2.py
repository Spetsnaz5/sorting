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
steps = []  # 儲存每一步的比較與交換

# 快速排序：記錄過程到 steps
def quick_sort(arr, low, high):
    if low < high:
        pivot_index = partition(arr, low, high)
        quick_sort(arr, low, pivot_index - 1)
        quick_sort(arr, pivot_index + 1, high)

def partition(arr, low, high):
    pivot = arr[high] # 選最後一個元素當基準
    i = low - 1
    for j in range(low, high):
        steps.append((arr.copy(), j, high))  # 比較 j 與 pivot
        if arr[j] < pivot:
            i += 1
            arr[i], arr[j] = arr[j], arr[i] # 交換
            steps.append((arr.copy(), i, j))  
    arr[i + 1], arr[high] = arr[high], arr[i + 1] # 最後交換 pivot
    steps.append((arr.copy(), i + 1, high))  
    return i + 1

# 執行排序
quick_sort(data.copy(), 0, len(data) - 1)

# 設定畫布
fig, ax = plt.subplots()
sc = ax.scatter(range(len(data)), data, c='skyblue', s=100)
ax.set_title("Quick Sort - Scatter Plot Animation")
ax.set_xlim(-1, len(data))
ax.set_ylim(0, max(data) + 20)

# 動畫更新函式
def update(frame):
    current, i, j = frame
    colors = ['red' if k == i or k == j else 'skyblue' for k in range(len(current))]
    sc.set_offsets([[x, y] for x, y in zip(range(len(current)), current)])
    sc.set_color(colors)
    ax.set_title(f"Comparing/Swapping: index {i} and {j}")

# 動畫執行
ani = animation.FuncAnimation(fig, update, frames=steps, interval=300, repeat=False)
plt.show()

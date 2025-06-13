"""
泡沫排序演算法的運作如下：
    比較相鄰的元素。如果第一個比第二個大，就交換它們兩個。
    對每一對相鄰元素作同樣的工作，從開始第一對到結尾的最後一對。這步做完後，最後的元素會是最大的數。
    針對所有的元素重複以上的步驟，除了最後一個。
    持續每次對越來越少的元素重複上面的步驟，直到沒有任何一對數字需要比較。
"""

import matplotlib.pyplot as plt
import matplotlib.animation as animation
import random

# 建立要排序的資料
data = [random.randint(10, 100) for _ in range(20)]

print(data)

def sort_steps(data):
    arr = data.copy()
    steps = []

    for i in range(len(arr)):
        for j in range(len(arr) - i - 1):
            # 儲存目前的狀態與高亮點
            steps.append((arr.copy(), j, j + 1))
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]
                steps.append((arr.copy(), j, j + 1))
                
    print(arr)
    return steps

steps = sort_steps(data)

# 畫布初始化
fig, ax = plt.subplots()
sc = ax.scatter(range(len(data)), data, c='skyblue', s=100)
ax.set_title("Bubble Sort - Scatter Plot Animation")
ax.set_xlim(-1, len(data))
ax.set_ylim(0, max(data) + 20)

# 動畫更新函式
def update(frame):
    current, i, j = frame
    colors = ['red' if k == i or k == j else 'skyblue' for k in range(len(current))]
    
    sc.set_offsets([[x, y] for x, y in zip(range(len(current)), current)])
    sc.set_color(colors)
    ax.set_title(f"Comparing: index {i} and {j}")

ani = animation.FuncAnimation(fig, update, frames=steps, interval=100, repeat=False)
plt.show()
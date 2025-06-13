"""
插入排序演算法的運作如下：
    1.在未排序序列中找到最小（大）元素，存放到排序序列的起始位置
    2.從剩餘未排序元素中繼續尋找最小（大）元素，然後放到已排序序列的末尾。
    3.重複步驟1~2，直到所有元素均排序完畢。
"""

import random
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# 隨機資料
data = [random.randint(10, 100) for _ in range(20)]

print(data)

def sort_steps(arr):
    n = len(arr)
    steps = []
    for i in range(n):
        min_idx = i
        for j in range(i + 1, n):
            steps.append((arr.copy(), min_idx, j))  # 比較 i, j
            if arr[j] < arr[min_idx]:
                min_idx = j
                
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
        steps.append((arr.copy(), i, min_idx))  # 交換後的結果

    print(arr)
    return steps

# 執行排序並記錄步驟
steps = sort_steps(data.copy())

# 畫布設定
fig, ax = plt.subplots()
sc = ax.scatter(range(len(data)), data, c='skyblue', s=100)
ax.set_title("Selection Sort - Scatter Plot Animation")
ax.set_xlim(-1, len(data))
ax.set_ylim(0, max(data) + 20)

# 更新動畫的函式
def update(frame):
    current, i, j = frame
    colors = ['red' if k == i or k == j else 'skyblue' for k in range(len(current))]
    sc.set_offsets([[x, y] for x, y in zip(range(len(current)), current)])
    sc.set_color(colors)
    ax.set_title(f"Comparing: index {i} and {j}")

# 動畫
ani = animation.FuncAnimation(fig, update, frames=steps, interval=100, repeat=False)
plt.show()
# 最大整數函數（Floor Function）定義如下:
# 對於任意實數 x，最大整數函數 f(x) = ⌊x⌋，表示不大於 x 的最大整數。
# 也就是說，將 x 向下取整。
# 例如：
#   f(4.7) = 4
#   f(-2.3) = -3
#   f(5) = 5

import numpy as np
import matplotlib.pyplot as plt

# 定義區間 -5/2 ≤ x ≤ 5/2
x = np.linspace(-5/2, 5/2, 1000)

# 應用最大整數函數 np.floor 將 x 向下取整
y = np.floor(x)

# 繪製圖形，並調整 x 軸和 y 軸的順序，使其不被覆蓋
plt.figure(figsize=(8, 6))

# 添加粗的 x 軸和 y 軸（優先繪製，避免被覆蓋）
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)

# 繪製分段函數
plt.step(x, y, where='post', label=r"$f(x) = \lfloor x \rfloor$", color='b', linewidth=2)

# 添加標題和標籤
plt.title(r"Graph of $f(x) = \lfloor x \rfloor$ in the interval $-\frac{5}{2} \leq x \leq \frac{5}{2}$")
plt.xlabel("x")
plt.ylabel(r"$\lfloor x \rfloor$")

# 添加網格和圖例
plt.grid(True)
plt.legend()

# 顯示圖形
plt.show()


# 題目:
# 將 f(x) = ⌊x⌋, 0 ≤ x < 3 化成分段定義函數，並畫出圖形。
# 其中 ⌊x⌋ 表示向下取整的最大整數函數。
# 化成分段定義函數後為:
# f(x) = {
#     0  當 0 ≤ x < 1
#     1  當 1 ≤ x < 2
#     2  當 2 ≤ x < 3
# }


import numpy as np
import matplotlib.pyplot as plt


#題目2 定義分段函數 f(x) 根據 x 的值在不同區間返回不同整數
def f(x):
    if 0 <= x < 1:
        return 0
    elif 1 <= x < 2:
        return 1
    elif 2 <= x < 3:
        return 2

# 使用 numpy 生成 x 值區間，並應用函數 f(x) 來計算對應的 y 值
x_values = np.linspace(0, 3, 1000)
y_values = [f(x) for x in x_values]

# 繪製圖形
plt.figure(figsize=(8, 6))
plt.step(x_values, y_values, where='post', label=r"$f(x) = \lfloor x \rfloor$", color='b', linewidth=2)

# 添加標題和標籤
plt.title(r"Graph of $f(x) = \lfloor x \rfloor$ for $0 \leq x < 3$")
plt.xlabel("x")
plt.ylabel(r"$f(x)$")

# 添加粗的 x 軸和 y 軸
plt.axhline(0, color='black', linewidth=2)
plt.axvline(0, color='black', linewidth=2)

# 添加網格和圖例
plt.grid(True)
plt.legend()

# 顯示圖形
plt.show()

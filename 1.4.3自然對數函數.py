import numpy as np
import matplotlib.pyplot as plt

# 自然對數函數的定義:
# 自然對數函數記作 ln(x)，其定義為:
# ln(x) = log_e(x)
# 其中 e 是自然常數，約等於 2.71828。
# 自然對數函數表示的是數 e 需要提高到多少次方才能等於 x：
# ln(x) = y  ⇔  e^y = x
# 自然對數函數的主要性質：
# 1. 定義域: x > 0，函數只對正數有效。
# 2. ln(1) = 0 因為 e^0 = 1。
# 3. ln(e) = 1 因為 e^1 = e。
# 4. 自然對數的導數: d/dx ln(x) = 1/x。
# 這是自然對數的定義部分。

# y = ln(x) 與 y = e^x 互為反函數，它們的圖形對稱於 y = x。
# 請繪製 y = ln(x) 和 y = e^x 的圖形，並畫出 y = x 作為對稱軸。
# 並顯示四個象限，以清楚展示這些函數的行為

# 定義 x 的範圍
x_values = np.linspace(0.1, 3, 400)  # 0.1 是為了避免 ln(0)
x_exp_values = np.linspace(-2, 3, 400)  # 擴展範圍適合 e^x 函數

# 計算 y = ln(x) 和 y = e^x
y_ln = np.log(x_values)
y_exp = np.exp(x_exp_values)

# 繪製圖形，擴大第四象限的範圍
plt.figure(figsize=(8, 8))

# y = ln(x) 的圖形
plt.plot(x_values, y_ln, label=r"$y = \ln(x)$", color='b', linewidth=2)

# y = e^x 的圖形
plt.plot(x_exp_values, y_exp, label=r"$y = e^x$", color='r', linewidth=2)

# y = x 的對稱軸
plt.plot(x_exp_values, x_exp_values, label=r"$y = x$", color='g', linestyle='--', linewidth=2)

# 繪製四個象限的 x 軸和 y 軸
plt.axhline(0, color='black', linewidth=1.5)
plt.axvline(0, color='black', linewidth=1.5)

# 擴大第四象限的範圍
plt.xlim(-2, 3)
plt.ylim(-2, 8)

# 添加標題和標籤
plt.title(r"Graphs of $y = \ln(x)$ and $y = e^x$ with symmetry about $y = x$")
plt.xlabel("x")
plt.ylabel("y")

# 添加網格和圖例
plt.grid(True)
plt.legend()

# 顯示圖形
plt.show()

# 自然對數的四個重要性質:
# (1) ln(x) + ln(y) = ln(xy), 當 x > 0 且 y > 0
#     這是對數的乘法性質，兩個數相乘的對數等於它們各自對數的和。
#
# (2) ln(x^r) = r * ln(x), 當 x > 0
#     這是對數的冪次性質，表示一個數的冪次對數等於該數的對數乘以冪指數 r。
#
# (3) ln(x) - ln(y) = ln(x / y), 當 x > 0 且 y > 0
#     這是對數的除法性質，兩個數相除的對數等於它們各自對數的差。
#
# (4) e^ln(x) = x, 當 x > 0
#     這是一個重要但經常被忽視的性質，說明自然對數和指數運算互為反函數。


# 定義自然對數和一般對數性質的運算

# 公式
# ln(x * y) = ln(x) + ln(y)
def natural_log_product(x, y):
    if x > 0 and y > 0:
        return np.log(x * y), np.log(x) + np.log(y)

# log_a(X) = ln(X) / ln(a)
def logarithm_base_a(a, x):
    if a > 0 and x > 0:
        return np.log(x) / np.log(a)

# 測試這兩個性質
x = 5
y = 3
a = 2

# 自然對數乘法性質
ln_product, ln_sum = natural_log_product(x, y)
print(f"ln({x} * {y}) = {ln_product}, ln({x}) + ln({y}) = {ln_sum}")

# 一般對數公式 log_a(x)
log_base_a = logarithm_base_a(a, x)
print(f"log_{a}({x}) = {log_base_a}")


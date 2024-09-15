"""
反函數的定義：
- 如果一個函數 f(x) 有反函數 f^{-1}(x)，那麼對於每個輸入 x 和對應的輸出 y，有以下關係：
  f(f^{-1}(x)) = x 且 f^{-1}(f(x)) = x。
- 換句話說，反函數 f^{-1}(x) 將 f(x) 的輸出還原為其輸入。

條件：
- 只有一對一函數才能擁有反函數，因為反函數需要對應唯一的輸出和輸入。

例子：
1. 如果 f(x) = 2x + 3，則它的反函數 f^{-1}(x) 是 (x - 3) / 2。
2. 如果 f(x) = x^2 (x >= 0)，則它的反函數 f^{-1}(x) 是 sqrt(x)。

"""

# 定義線性函數 f(x) = 2x + 3
def f(x):
    """
    函數 f(x) 的定義:
    - 這是一個線性函數: f(x) = 2x + 3
    """
    return 2 * x + 3

# 定義反函數 f_inverse(x)
def f_inverse(y):
    """
    函數 f_inverse(y) 的定義:
    - 這是線性函數 f(x) = 2x + 3 的反函數:
      f_inverse(x) = (x - 3) / 2
    - 解 f(x) = 2x + 3 得出反函數:
      y = 2x + 3 -> x = (y - 3) / 2
    """
    return (y - 3) / 2

# 測試 f(x) 和 f_inverse(x) 的互逆性
x_value = 5
y_value = f(x_value)
x_recovered = f_inverse(y_value)

print(f"當 x = {x_value} 時，f(x) = {y_value}")
print(f"當 y = {y_value} 時，f_inverse(y) = {x_recovered}")
print(f"檢查: f(f_inverse({y_value})) = {f(x_recovered)} (應等於 {y_value})")
print(f"檢查: f_inverse(f({x_value})) = {x_recovered} (應等於 {x_value})")

# 測試平方根的反函數
import math

# 定義平方函數 f(x) = x^2, 並限制 x >= 0 使其為一對一函數
def square(x):
    """
    函數 square(x) 的定義:
    - 這是一個平方函數: f(x) = x^2 (定義域 x >= 0)
    """
    return x ** 2

# 定義平方根函數作為反函數
def square_inverse(y):
    """
    函數 square_inverse(y) 的定義:
    - 這是平方函數的反函數: f_inverse(y) = sqrt(y)
    - 注意這只適用於非負數 y (y >= 0)
    """
    return math.sqrt(y)

# 測試平方函數和平方根函數的互逆性
x_value = 4
y_value = square(x_value)
x_recovered = square_inverse(y_value)

print(f"\n當 x = {x_value} 時，f(x) = {y_value}")
print(f"當 y = {y_value} 時，f_inverse(y) = {x_recovered}")
print(f"檢查: square(square_inverse({y_value})) = {square(x_recovered)} (應等於 {y_value})")
print(f"檢查: square_inverse(square({x_value})) = {x_recovered} (應等於 {x_value})")

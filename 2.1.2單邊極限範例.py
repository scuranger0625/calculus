import numpy as np

# 定義函數 f(x) = 3x - 1
def f(x):
    return 3 * x - 1

# 定義 epsilon 為非常小的值，這裡設置為 0.1
epsilon = 0.1

# 右極限：當 x -> 2^+，即 x = 2 + epsilon
x_right = 2 + epsilon
right_limit = f(x_right)

# 左極限：當 x -> 2^-，即 x = 2 - epsilon
x_left = 2 - epsilon
left_limit = f(x_left)

# 輸出結果
print(f"當 epsilon = {epsilon} 時：")
print(f"右極限 (x -> 2^+) = f(2 + {epsilon}) = {right_limit}, 因趨近於 2 所以取值為 {int(right_limit)}")
print(f"左極限 (x -> 2^-) = f(2 - {epsilon}) = {left_limit}, 因趨近於 2 所以取值為 {int(left_limit)}")

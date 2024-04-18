# @Version  : 1.0
# @Author   : 韩顺平

# 打印40-200之间所有的偶数
"""
    思路分析:
    1. 定义 i = 40 max_num = 200, 表示我们要遍历的范围while
    2. 如果 i % 2 == 0, 说明当前i是偶数
    3. 满足条件输出即可  , 注意遍历时 i += 1
"""

i = 40
max_num = 200
# 遍历40 -200
while i <= max_num:
    # 如果i 是偶数
    if i % 2 == 0:
        print(i)
    i += 1

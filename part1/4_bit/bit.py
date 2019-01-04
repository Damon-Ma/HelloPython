'''

位运算
'''

# 按位与运算 &
i = 11  # 1011
print(bin(i))
j = 2   # 0010
print(bin(j))
z = i & j   # 0010
print(z)
print(bin(z))

# 按位或运算 |
z = i | j   # 1011
print(z)
print(bin(z))

# 按位异或运算 ^
z = i ^ j   # 1001
print(z)
print(bin(z))

# 按位取反运算 ~
z = ~ i     # -i-1
print(z)
print(bin(z))

# 左移运算符 <<
z = i << 2  # 101100
print(z)
print(bin(z))

# 右移运算符号 >>
z = i >> 2  # 0010
print(z)
print(bin(z))
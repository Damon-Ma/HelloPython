'''

进制运算
10进制 2进制 8进制 16进制
'''

# 十进制转其他进制

# 十进制转2进制
i = 16
j = bin(i)  #0b10000   0b代表二进制
print(j)

# 十进制转换8进制
j = oct(i)  #0o20   0o 代表8进制
print(j)

#十进制转换16进制
j = hex(i)  #0x10   0x代表16进制
print(j)

# 二进制转10进制
i = '10'
j = int(i, 2)
print(j)

# 八进制转10进制
j = int(i, 8)
print(j)

# 十六进制转10进制
j = int(i, 16)
print(j)



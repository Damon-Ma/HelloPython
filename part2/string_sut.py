# 声明一个字符串

# 单引号声明
s = 'Hello Python'
print(s)

# 双引号说明
s = "Hello Python"
print(s)

# 三引号声明
s = """Hello
Python
"""
print(s)

# 字符串操作

# 单个访问字符串中的字符
s = 'Hello Python'
print(s[0])

# 切片操作  【左闭右开原则】
print(s[0:5])
print("------------------", s.split(" "))
# 字符串相加
s1 = 'Hello'
s2 = ' Python'
print(s1+s2)

# 字符串更新
s1 = 'Hello String'
s2 = 'Python'
print(s1[0:6] + s2)

# 字符串的成员运算
s1 = 'Hello Python'

#包含运算
s2 = 'H'
print(s2 in s1)

# 不包含运算
print(s2 not in s1)

# 转义字符
print(" ' ")
print(" \" ")
print("Hello\nPython")  #换行符
print("Hello\tPython")  #制表符
print("Hello\rPython")  #回车符   光标到行首，只打印 \r 后的内容
# 原始字符串
print(r'Hello\nPython')
print(R'Hello\nPython')

# 字符串的格式化输出 我叫Damon，今天是我第1天学Python
print('我叫%s，今天是我第%d天学Python' % ('Damon', 2))

# 字符串的内建函数

# 查找字符串
s = 'Hello Python'
print(s.find('n'))  # 返回所查找字符的位置

# 转换大小写
print(s.lower())    # 转换为小写
print(s.upper())    # 转换为大写

# 返回字符串长度,他返回的是字符串的自然长度
print(s.__len__())

# 判断字符串是否 只 包含空格
print(' '.isspace())
print(' a '.isspace())

# 字符串替换
print(s.replace('o', 'ee'))

# python 自带学习文档 python3 -m pydoc -p 8888

'''

集合：无序的不重复元素的序列
    两种声明方法:
    1.{}
    2.set()
'''

# 声明一个集合
set_param = {'java', 'python', 'php', 'java'}
print(set_param)

# 判断元素是否在集合内
print('java' in set_param)
print('c' in set_param)

# 两个集合间的运算

a = set('abcdefg')
b = set('abcxyz')
print(a)
print(b)

print(a & b)
print(a | b)
print(a ^ b)

# 集合添加元素
my_set = set(('java', 'python', 'php'))
my_set.add('c')
print(my_set)

# 移除元素
my_set.remove('php')
print(my_set)

# 随机移除一个元素
print(my_set.pop())
print(my_set)

# 计算集合的个数
print(my_set.__len__())

# 清空集合
my_set.clear()
print(my_set)




'''
字典：一种可变容器类型，也是可以存储任意类型的对象

'''

d = {'java': 22, 'python': 23, 'php': 18}
print(d)

# 访问
keys = d.keys()
print(keys)
print(d['java'])

# 增加
d['c'] = 25
print(d)

# 更新
d['python'] = 28
print(d)

# 删除
del d['php']
print(d)

# 判断键是否在字典中
print('java' in d)

# 清空字典
d.clear()
print(d)



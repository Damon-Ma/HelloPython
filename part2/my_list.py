'''
列表：一组数据
list是有序的序列，序列中每个元素分配一个数字，也叫索引，位置角标，左边
他是从0开始的
'''
list1 = ['Java', 22, 'python', 25, 'php', 21]
print(type(list1))
print(list1)

# 访问列表
print(list1[0])
print(list1[2:])    # 左闭右开

# 列表更新
list1[1] = 23
print(list1)

# 列表添加
list1.append('c')
list1.append(30)
print(list1)

list1 = list1 + ['c++', 22]
print(list1)

# 删除操作
del list1[6]
print(list1)

# 移除某个元素
list1.remove(30)
print(list1)

# 嵌套列表
list1 = [['java', 'python', 'php'], [18, 20, 22]]
print(list1)
print(list1[0])
print(list1[0][0])

# 返回列表元素的个数
print(list1.__len__())

# 移除列表中的元素
print(list1.pop(1))     # 移除列表中的元素，并且返回移除的值
print(list1)

# 对列表中的元素进行排序
list1 = [12, 22, 11, 14]
list1.sort()
print(list1)

# 查找列表中第一个匹配的元素索引值
list1 = [12, 22, 11, 14]
print(list1.index(22))



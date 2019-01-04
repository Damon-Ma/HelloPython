'''

条件控制
    1.比较运算符：
        == > < <= >= !=

'''

i = 'a'
j = 'B'

if i > j:
    print('a大')
else:
    print('B大')

'''
ASCII 码表
'''
# 转ASCII码
print(ord(i))
print(ord(j))
# ASCII码转字符
print(chr(97))

'''
成员运算符
    in 、not in
'''

my_string = 'abcdxyz'
if 'a' in my_string:
    if 'b' in my_string:
        print('ab都在')
if 't' not in my_string:
    print('t不在')

'''
逻辑运算符
and 、 or 、 not
'''
if 'a' in my_string and 'b' in my_string:
    print('ab都在')

'''
真假值的判断

大于0的数字返回true，0代表false
and 需要判断到最后一个值，只有全部为真时才会返回真
or 只要碰到真值就直接返回真，剩下的不再判断

'''
print(True and False)
print(True or False)
print(not True)

print(1 and 0)
print(1 or 0)
print(not 1)

'''
身份运算符
is 、is not

'''
i = 1
j = 1
print(i == j)
print(i is j)
# 取地址
print(id(i))
print(id(j))

j += 1
print(id(j))

list1 = [1, 2, 3]
list2 = [1, 2, 3]

print(id(list1))
print(list1 == list2)
print(id(list2))
print(list1 is list2)




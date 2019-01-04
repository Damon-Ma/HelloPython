'''
循环
while
for

'''

# while 求1-10的和
i = 1
count = 0
while i <= 10:
    count += i
    i += 1
print(count)

# for
list1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
count = 0
for i in list1:
    count += i
print(count)

count = 0
for i in range(11):
    count += i
print(count)

# 循环的中断  break continue

'''
冒泡排序
[2,1,4,7,12,3]

'''
nums = [2, 1, 4, 7, 12, 3]

# 从小到大排序
for i in range(nums.__len__() - 1):
    for j in range(nums.__len__() - i - 1):
        if nums[j] > nums[j+1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)

# 从大到小排序
for i in range(nums.__len__() - 1):
    for j in range(nums.__len__() - i - 1):
        if nums[j] < nums[j + 1]:
            nums[j], nums[j+1] = nums[j+1], nums[j]
print(nums)

# 插入num
num = 9
for i in range(nums.__len__()-1):
    if nums[i] < num:
        nums.insert(i, num)
        break
    elif nums[nums.__len__()-1] >= num:
        nums.insert(nums.__len__(), num)
        break
print(nums)

num = 0
for i in nums:
    if i <= num:
        nums.insert(nums.index(i), num)
        break
        # nums.insert(nums.index(i), num)
    elif nums[nums.__len__()-1] > num:
        nums.insert(nums.__len__(), num)
        break
print(nums)








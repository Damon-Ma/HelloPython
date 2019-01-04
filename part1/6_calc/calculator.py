'''
作业：根据学过的运算符，完成一个计算器后台算法开发
'''

while True:
    first_number = input("请输入第一个数字：")
    operation = input("请输入运算符：")
    second_number = input("请输入第二个数字：")

    # 类型转换
    if "." in first_number or "." in second_number:
        first_number = float(first_number)
        second_number = float(second_number)
    else:
        first_number = int(first_number)
        second_number = int(second_number)

    if operation == "+":
        result = first_number + second_number
    elif operation == "-":
        result = first_number - second_number
    elif operation == "*":
        result = first_number * second_number
    elif operation == "/":
        result = first_number / second_number
    elif operation == "%":
        # 取模运算
        result = first_number % second_number
    elif operation == "**":
        # 取幂运算
        result = first_number ** second_number
    elif operation == "//":
        # 整除
        result = first_number // second_number
    elif operation == "+=":
        first_number += second_number
        result = first_number
    elif operation == "-=":
        first_number -= second_number
        result = first_number
    elif operation == "*=":
        first_number *= second_number
        result = first_number
    elif operation == "/=":
        first_number /= second_number
        result = first_number
    else:
        print("运算符输入错误！！")
        result = 'error'

    print("计算结果是：" + str(result))

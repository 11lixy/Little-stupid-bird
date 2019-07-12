current_number = 1
while current_number <= 5:#while函数循环
    print(current_number)
    current_number += 1#current_number = current_number + 1的简写

#在循环中使用continue
current_number = 0
while current_number <10:#小于10，进入循环
    current_number += 1#current_number = current_number + 1的简写
    if current_number % 2 == 0:#if语句检查current_number与2的求模运算（求模运算符%，将两个数相除并返回余数），如果结果为
        #0（current_number可被2整除)，就执行continue语句，忽略余下的代码，返回到循环的开头，不能被2整除，就执行循环中余下
        #的代码，将这个数字打印出来。
        continue#返回到循环开头，根据条件测试结果决定是否继续执行循环，使用continue语句
    print(current_number)

#避免无限循环
x = 1
while x <= 5:
    print(x)
    x += 1
#如果你遗漏了x += 1 这行代码，这个循环将没完没了的运行
x = 1
while x <= 5:
    print(x)
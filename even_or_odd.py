number = input("Enter a numbr, and I'll tell you if it's even or odd: ")#input让程序暂停运行，等待用户输入一些文本
number = int(number)#函数int()将输入转换为数值

if number % 2 == 0:#运算符%将两个数相除，返回余数.一个数number和2执行求模运算，余数为0，就是偶数。
    print("\nThe number " + str(number) + " is even.")#str函数转换为字符串输出
else:
    print("\nThe number " + str(number) + " is odd.")
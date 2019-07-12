height = input("How tall are you, in inches?")#input让程序暂停运行，等待用户输入一些文本
height = int(height)#函数int()将输入转换为数值

if height >= 36:
    print("\nYou're tall enough to ried!")
else:
    print("\nYou'll be able to ride when you're a little older.")
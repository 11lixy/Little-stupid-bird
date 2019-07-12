#习题7-1
cars = input("What kind of car do you want to rent?")#input让程序暂停运行，等待用户输入一些文本
print("Let me see if I can find you a Subaru.")
#习题7-2
restaurant = input("How many of you eat?")
restaurant = int(restaurant)
if restaurant > 8:
    print("There are no vacant tables.")
else:
    pritn("Free table.")
#习题7-3
number = input("Enter a number:")
number = int(number)
if number % 10 ==0:
    print("是10的倍数")
else:
    print("不是")
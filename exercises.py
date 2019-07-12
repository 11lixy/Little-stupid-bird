#7-4-披萨配料
active = True
while active:
    inquiry = input("请输入披萨配料：")
    if inquiry == 'quit':
        active = False
    else:
        print("我们加入该配料。")

#7-5-电影票
active = True
while active:
    age = input("你多少岁？")
    if int(age) < 3:
        print("免费")
    elif int(age)  <= 12:
        print("你要支付10美金")
    else:
        print("你要支付15美金")

#7-6-三个出口
active = True
while active:
    inquiry = input("请输入披萨配料：")
    if inquiry == 'quit':
        break
    else:
        print("我们加入该配料。")




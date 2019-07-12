#使用break退出循环
prompt = "\nPlease enter the name of a city you have visited:"
prompt += "\n(Enter 'quit' when you are finished.)"
while True:
    city = input(prompt)
    if city =='quit':
        break#用户输入quit后，执行break语句，退出循环
    else:
        print("I'd love to go to " + city.title() + "!")
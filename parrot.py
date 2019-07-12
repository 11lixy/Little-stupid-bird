prompt = "\nTell me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program."
message = "" #定义一个变量message，值为空
while message != 'quit':#只要message值不是quit，while循环就会不断运行
    message = input(prompt)#等待用户输入，不管用户输入的什么都将存储到变量message中并打印，只要用户输入的不是‘quit’，
    # 就会再次显示提示消息并等待用户输入
if message != 'quit':
    print(message)
#使用标志
prompt = "\nTell me something, and I will repeat it back to you:"
prompt +="\nEnter 'quit' to end the program."
active = True#把这个标志命名为active（可以指定任何名称），将变量active设置为True，只要变量active为True，循环就继续运行
while active:
    message = input(prompt)
    if message == 'quit':#如果用户输入的是quit，就将变量active设置为False，循环就不再继续执行
        active = False
    else:#如果用户输入的不是quit，我们就将输入作为一条消息打印出来
        print(message)
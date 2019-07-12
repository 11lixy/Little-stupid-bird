#函数input()让程序暂停运行，等待用户输入一些文本。获取用户输入后，python将其存储在一个变量中，方便使用
name = input("Please enter your name: ")
print("Hello, " + name + "!")

prompt = "If you tell us who you are, we can personalize the messages you see."#将消息的前半部分存储在变量prompt中
prompt += "\nWhat is your first name? "#+=在存储在prompt中的字符串末尾附加一个字符串
name = input(prompt)
print("\nHello," + name + "!")

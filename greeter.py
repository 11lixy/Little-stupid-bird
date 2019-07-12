def greet_user():#使用def定义一个函数，向python指出了函数名，还可能在括号内指出函数为完成其任务需要什么样的信息。
    #后面的缩进构成了函数体
    """显示简单的问候语"""#此处被称为文档字符串的注释，描述了函数是做什么的，文档字符串用三引号括起，python使用它们来生
    # 成有关程序中函数的文档
    print("Hello!")

greet_user()#要使用函数要调用它，函数调用让python执行函数的代码。调用函数，依次指定函数名以及用括号括起的必要信息，由于
# 这个函数不需要任何信息，因此只需输入greet_user()即可


#像函数传递信息，只要稍作修改，就可以让函数greet_user()不仅向用户显示Hello！，还将用户的名字用做抬头。为此，可在函数定义
#def greet_user()的括号内添加username。通过在这里添加username，就可以让函数接受你给username指定的任何值。
def greet_user(username):
    """显示简单的问候语"""
    print("Hello, " + username.title() + "!")
greet_user('李')
#调用函数greet_user()，并向它提供执行python语句所需的信息。这个函数接受你传递给他的名字，并向这个人发出问候
greet_user('陈')

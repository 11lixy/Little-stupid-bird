#7-8
sandwich_orders = ['Vegetable sandwiches','Beef sandwich','Ham sandwich']#创建一个列表
finished_sandwiches = []
while sandwich_orders:
    finished_sandwiches = sandwich_orders.pop()#pop()函数以每次一个的方式从列表sandwich_orders末尾删除列表里的元素，存储
                                                # 到变量finished_sandwiches
    print("I made your " + finished_sandwiches.title())
    print("有这些三明治您可以选择:" + finished_sandwiches.title())#title所有首字母大写
#7-9
sandwich_orders = ['Vegetable sandwiches','pastrami','Beef sandwich','Ham sandwich','pastrami','pastrami']#创建一个列表
finished_sandwiches = []
print("\n五香烟熏牛肉（pastrami）卖完了")
while 'pastrami' in sandwich_orders:
    sandwich_orders.remove('pastrami')
print(sandwich_orders)
while sandwich_orders:
    sandwich = sandwich_orders.pop()
    finished_sandwiches = sandwich.append()
print(finished_sandwiches)



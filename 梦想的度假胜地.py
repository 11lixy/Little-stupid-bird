places = {}
#设置一个标志，指出调查是否继续
avtive = True
while avtive:
    name = input("你的名字是：")
    place = input("如果你能在这个世界上找到一个地方，你会去哪里？")
    #将答案存储在字典中
    places[name] = place
    #看看是否有人还要参加
    repeat = input("你想让其他人回答吗？(是/不想)")
    if repeat == '不想':
        avtive = False

#调查结果
print("\n---调查结果---")
for name,place in places.items():#items以列表形式返回可遍历的(键, 值) 元组数组
    print(name + " 想旅游吗？ " + place +"." )







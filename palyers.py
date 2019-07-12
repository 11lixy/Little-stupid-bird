players = ['charles','michael','florence','eli']
print(players[0:3])#创建切片，使用第一个元素的索引和最后一个元素的索引加1
players2 = ['charles','michael','florence','eli','michael']#这里我们用切片输出包含前四名的一个列表
print(players2[0:5])#最后一个元素的索引加一，所以是5
print(players2[1:5])
print(players2[:4])#如果没有指定其实索引，从列表开头开始提取
print(players2[2:])#没有后面元素的索引，直接终止与列表末尾
print(players2[-3:])#可以使用副索引
#遍历切片
players3 = ['charles','michael','michael','florence','eli']
print("Here are the first three players on my team:")
for player in players3[:3]:
	print(player.title())

my_pizzas = ['ham pizza','beef pizza','potato pizza']
friend_pizzas = my_pizzas[:]#要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]），这让python创建一个始于第一个元素，终止与最后一个元素的切片，即复制整个列表
my_pizzas.append('tomato pizza')#使用.append将元素添加到列表的末尾
friend_pizzas.append('vegetable pizza')#使用.append将元素添加到列表的末尾
print("My favorite pizzas are:")
for my_pizza in my_pizzas:
	print(my_pizza)
print("\nMy_friend's favorite pizzas are:")
for friend_pizza in friend_pizzas:
	print(friend_pizza)

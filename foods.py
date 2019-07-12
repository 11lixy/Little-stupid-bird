my_foods = ['pia','falafel','carrot cake']
friend_foods = my_foods[:]#要复制列表，可创建一个包含整个列表的切片，方法是同时省略起始索引和终止索引（[:]），这让python创建一个始于第一个元素，终止与最后一个元素的切片，即复制整个列表
my_foods.append('cannoli')#使用.append将元素添加到列表的末尾
friend_foods.append('ice cream')#使用.append将元素添加到列表的末尾
print("My favorite foods are:")
for food in my_foods:
	print(food)
print("\nMy friend's favorite foods are:")
for food in friend_foods:
	print(food)

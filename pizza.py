# 存储所点披萨的信息
#首先创建一个字典
pizza = {
	'crust':'thick',
	'toppings':['mushrooms','extra cheese'], #键是toppings，值是一个列表
	}

#概述所点的披萨
print("You ordered a " + pizza['crust'] + "-crust pizza" + 
	"with the following toppings:")
for topping in pizza['toppings']:
	print("\t" + topping)#\t横向制表符
	

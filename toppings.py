requested_toppings = ['mushrooms','green peppers','extra cheese']
for requested_topping in requested_toppings:
	print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
#如果披萨店的青椒用完了，可以在for循环中加if语句

for requested_topping in requested_toppings:
	if requested_topping == 'green peppers':#检查顾客点的是不是青椒，是就打印一条消息
		print("Sorry,we are out of green peppers right now.")
	else:#此处确保其他的配料都添加到披萨中
		print("Adding " + requested_topping + ".")
print("\nFinished making your pizza!")
#确定列表不是空的的
requested_toppings = []
if requested_toppings:#我们进行简单检查，而不是执行for循环
	for requested_topping in requested_toppings:
#在if语句中将列表名用在条件表达式中时，python将在列表至少包含一个元素时返回true，并在
#列表为空时返回false。如果列表不为空，就运行与前一个示例相同的for循环。
		print("Adding " + requested_topping + ".")
	print("\nFinished making your pizza!")
else:
	print("Are you sure you want a plain pizza?")
#否则就打印一条消息，询问顾客是否确实要点不加任何配料的披萨。

#使用多个列表
available_toppings = ['mushrooms','olives','green peppers','pepperoni',
'pineapple','extra cheese']
requested_toppings = ['mushrooms','french fries','extra cheese']	
for requested_topping in requested_toppings:
	if requested_topping in available_toppings:
		print("Adding " + requested_topping + ".")
	else:
		print("Sorry,we don't have " + requested_topping + ".")
		print("\nFinished making your pizza!")
	

	

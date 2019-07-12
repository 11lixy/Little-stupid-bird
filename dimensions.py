dimensions = (200,50)#元组看起来犹如列表，但使用圆括号而不是方括号来标识
print(dimensions[0])
print(dimensions[1])
for dimension in dimensions:
	print(dimension)#向列表一样，也可以使用for循环遍历元组中的所有值
print("Original dimensions:")
for dimension in dimensions:
	print(dimension)
dimensions = (400,100)
print("\nModified dimensions:")
for dimension in dimensions:
	print(dimension)

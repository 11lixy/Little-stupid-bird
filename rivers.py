rivers = {
	'nile':'egypt',
	'yangtze river':'china',
	'severn river':'britain',
	}
#循环遍历字典，要声明两个变量，这里的变量是key，value，用于存储键-值对中的键和值
for key,value in rivers.items():#items() 函数以列表返回可遍历的(键, 值) 元组数组。
	print("The " + key.title() + "runs through " + value.title())
	
for key in rivers.keys():#遍历所有的键
	print("\n"+key.title())

for value in rivers.values():#遍历所有的值
	print("\n"+value.title())

	

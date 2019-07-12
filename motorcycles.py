motorcycles = ['HONDA','YAMAHA','KTM']
print(motorcycles)
motorcycles[2] = 'DUCATI'
print(motorcycles)
motorcycles.append('suzuki')#append()为在其末尾添加元素
print(motorcycles)
motorcycles.insert(0,'BMW')
print(motorcycles)#insert()可以在列表任何位置添加新元素
del motorcycles[0]#使用del语句删除元素
print(motorcycles)
#下面是使用pop()删除元素，删除的值存储在变量poped_motorcycles1中,pop()括号里是元素的索引
motorcycles1 = ['honda','yamaha','suzuki']
poped_motorcycles1 = motorcycles1.pop(0)
print(motorcycles1)
print(poped_motorcycles1)
#根据值删除元素，用remove()
motorcycles2 = ['honda','yamaha','suzuki']
motorcycles2.remove('yamaha')
print(motorcycles2)




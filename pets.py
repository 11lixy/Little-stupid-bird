#while循环删除包含特定值的所有列表元素
pets = ['dog','cat','dog','goldfish','cat','rabbit','cat']
print(pets)

while 'cat' in pets:#循环列表里的一个值
    pets.remove('cat')#remove()函数删除列表里的特定值
print(pets)
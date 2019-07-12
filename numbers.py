for value in range(1,5):#使用range()函数打印数字
	print(value)
numbers = list(range(1,6))#使用list()将range()的结果转换为列表
print(numbers)
even_numbers = list(range(2,11,2))#打印10以内的偶数，一次加二，直到达到或超过终值(11)
print(even_numbers)
squares = []#首先我们创建一个空列表
for value in range(1,11):#接下来，使用range()函数遍历1～10的值
	s = value**2#在循环中，计算值的平方存储在变量s中
	squares.append(s)#将新计算得到的平方值附加到列表squares末尾
print(squares)#最后，循环结束，打印列表
squares = [value**2 for value in range(1,11)]#列表解析将for循环和创建新元素的代码合并成一行，并自动附加新元素
print(squares)
digits = [1,2,3,4,5,6,7,8,9,0]
min(digits)#最小的值
max(digits)#最大的值
sum(digits)#求和


for i in range(1,21):
	print(i)
numbers = []
for numbers in range(1,1000001):
	print(numbers)
number = list(range(1,1000001))#使用list()将range()的结果转换为列表
print(number)
print(min(number))
print(max(number))
print(sum(number))
s = list(range(1,21,2))
print(s)
n = list(range(3,31,3))
for n1 in n:
	print(n1)
q = []
for value in range(1,11):
	p = value**3
	q.append(p)
	print(q)
q = [value**3 for value in range(1,11)]
print(q)


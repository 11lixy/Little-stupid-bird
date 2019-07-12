motos = ['yamaha','suzuki','honda','ducati','kawasaki']
for moto in motos:
	if moto == 'yamaha':
		print(moto.upper())#检查当前汽车是不是为雅马哈，如果是就以全大写的方法打印
	if moto == 'suzuki':
		print(moto.upper())
	if moto == 'honda':
		print(moto.upper())
	if moto == 'ducati':
		print(moto.upper())
	if moto == 'kawasaki':
		print(moto.upper())
		
age1 = 'lxy'
age2 = 'Lxy'
#检查两个字符串相等和不等
print(age1 == age2)
#使用函数lower()测试,可以转换为小写
print(age1 == age2.lower())

number1 = 5
number2 = 10
#数字比较
print(number1 == number2)
print(number1 != number2)
print(number1 > number2)
print(number1 < number2)
print(number1 >= number2)
print(number1 <= number2)
#使用关键字and和or来测试
number = 5
number3 = 10
if number > 5 and number3 > 5:
	print("This is true")
else:
	print("This is False")
if number > 5 or number3 > 5:#or只要有一个条件成立就可以
	print("This is true")
else:
	print("This is False")
#测试特定的值是否包含在列表中，用关键字in
names = ['l','k','a','c','e']
print('b' in names)
print('a' in names)

	
		
	
		
	
	
	
		



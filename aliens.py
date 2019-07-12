#嵌套
#首先创建3个字典，每个字典表示一个外星人
alien_0 = {'color':'green','points':5}
alien_1 = {'color':'yello','points':10}
alien_2 = {'color':'red','points':15}
aliens = [alien_0,alien_1,alien_2]#将字典放在列表中
for alien in aliens:#遍历这个列表
	print(alien)

#创建一个用于存储外星人的空列表
aliens = []

#创建30个绿色的外星人
for alien_number in range(30):#range()返回一系列数字，告诉我们重复这个循环多少次
	new_alien = {'color':'green','points':5,'speed':'slow'}#每次执行这个循环时，创建一个外星人
	aliens.append(new_alien)#append将元素添加到已有list的末尾。                  并将其附加到aliens末尾
	
#显示前五个外星人
for alien in aliens[:5]:#使用切片打印前5个外星人
	print(alien)
print("...")

#显示创建了多少个外星人
print("Total number of aliens: " + str(len(aliens)))#打印列表的长度，证明确实创建了30个外星人
                                       #len() 方法返回对象（字符、列表、元组等）长度或项目个数


#创建一个用于存储外星人的空列表
aliens = []
#创建30个绿色的外星人
for alien_number in range(0,30):
	new_alien = {'color':'green','points':5,'speed':'slow'}
	aliens.append(new_alien)#append将元素添加到已有list的末尾。
for alien in aliens[0:3]:#我们要修改前3个外星人，需要遍历一个只包含这些外星人的切片
	if alien['color']=='green':#我们确保只修改颜色为绿色的外星人
		alien ['color'] = 'yellow'#如果外星人颜色是绿的我们改为黄色的
		alien['speed']= 'medium'
		alien['points'] = 10#将点数改为10
#显示前五个外星人
for alien in aliens[0:5]:
	print(alien)
print("...")

	

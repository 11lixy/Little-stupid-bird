alien_0 = {'color':'green','points':5}#字典用放在花括号{}中的一系列键-值对表示，
#键-值对是两个相关联的值。键和值之间用冒号分隔，键-值对之间用逗号分隔。
print(alien_0['color'])
#要获取与键相关联的值，可以指定字典名和放在方括号内的键，这将返回字典中与键相关联的值
print(alien_0['points'])
new_points = alien_0['points']#将与键points所关联的值存储在变量new_points
print(" You just earned " + str(new_points) + " points !")#str将整数转换为
#字符串，并打印一条消息，指出玩家获得多少个点

#添加键_值对
alien_1 = {'color':'red','points':5}
print(alien_1)
#下面在字典alien_1中添加两项信息
alien_1['x_position'] = 0   #外星人的x坐标，由于屏幕坐标系的原点通常为左上角，可将
#x坐标设置成0
alien_1['y_position'] = 25  #外星人的y坐标，将该外星人放在离屏幕顶部25像素的地方，
#可将y坐标设置为25
print(alien_1)#打印字典

alien_2 = {}#先创建一个空字典，先使用一对空的花括号定义一个字典
alien_2['color'] = 'green'#在分行添加各个键-值对
alien_2['points'] = 5
print(alien_2)

#修改字典中的值
#修改字典中的值，可以依次指定字典名，用方括号括起的键以及与该键相关联的新值
alien_3 = {'color':'green'}
print("The alien is " + alien_3['color'] + ".")
#我们将与键‘color’相关联的值改为‘red’
alien_3['color'] = 'red'
print("The alien is now " + alien_3['color'] + ".")

#删除键-值对
alien_4 = {'color':'green','points':5}
print(alien_4)
#使用del语句可以将相应的键-值对彻底删除，使用时必须指定字典名和要删除的键
del alien_4['points']#注意，删除的键-值对永远消失了
print(alien_4)

#使用字典存储众多对象的同一种信息
favorite_languages = {
	'lxy':'python',
	'lb':'java',
	'lm':'c++',
	'nx':'c',
	}
#确定使用多行定义字典时，在输入花括号后按回车，在下一行缩进4个空格，指定第一个键-值对，并
#在后面加上一个逗号，在按回车时，自动缩进后续键-值对，且缩进量与第一个键-值对相同
print("Lxy's favorite language is " + favorite_languages['lxy'].title()
	+ ".")
#为获悉lxy喜欢的语言我们用favorite_languages['lxy']


favorite_languages = {
	'j':'python',
	'k':'c++',
	'l':'js',
	'm':'ruby',
	}
friends = ['a','b']
for name,in favorite_languages.keys():#遍历所有的键，存储到变量name里
	print("Thank you " + name.title() + ".")
#使用keys()确定某个人是否接受了调查
if 'a' not in favorite_languages.keys():#核实o在不在包含的这个字典中
	print("\n"+"A,please take our poll!")
		


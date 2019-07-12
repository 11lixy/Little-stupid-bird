#遍历所有的键-值对
user_0 = {
	'username':'efermi',
	'first':'enrico',
	'last':'fermi',
	}
#循环遍历字典，要声明两个变量，这里的变量是key，value，用于存储键-值对中的键和值
for key,value in user_0.items():#items() 函数以列表返回可遍历的(键, 值) 元组数组。
	print("\nkey:" + key)
	print("Value:" + value)
	
#遍历字典中的所有键
favorite_languages = {
	'j':'python',
	'k':'c',
	'l':'js',
	'm':'c++',
	}
friends = ['j','s']
for name in favorite_languages.keys():#遍历所有的键，存储到变量name里
	print("\n"+name.title())

	if name in friends:#检查当前名字是否在列表friends中，如果在，就打印一句问候语
		print("Hi " + name.title() + ", I see your favorite language is "
			+ favorite_languages[name].title() + "!")
#使用keys()确定某个人是否接受了调查
if 'o' not in favorite_languages.keys():#核实o在不在包含的这个字典中
	print("\n"+"o,please take our poll!")

#按顺序遍历字典中的所有键
favorite_languages = {
	'j':'python',
	'k':'c',
	'l':'js',
	'm':'c++',
	}
for name in sorted(favorite_languages.keys()):#sorted()函数遍历前对这个列表进行排序
	print(name.title() + ",thank you for taking the poll.")
	
#遍历字典中所有的值
favorite_languages = {
	'j':'python',
	'k':'c',
	'l':'js',
	'm':'c++',
	}
print("The following languages have been mentioned:")
for language in favorite_languages.values():#提取字典里的每个值，存储在变量
#language中
	print(language.title())
	
favorite_languages = {
	'j':'python',
	'k':'c',
	'l':'js',
	'm':'python',
	}
print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):#函数set()会找出重复的元素，
#输出后是一个不重复的列表
	print(language.title())


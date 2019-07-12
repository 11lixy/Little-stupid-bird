#习题.使用一个字典存储一个熟人的信息，包括姓，名，年龄，居住的城市
acquaintance_information = {'last_name':'l','first_name':'xy','age':'16',
							'city':'suiping'}
print(acquaintance_information)

#习题.喜欢的数字
favorite_numbers = {
	'lxy':'0',
	'lb':'2',
	'lm':'1',
	'nx':'4',
	'cjb':'7',
	}
#为获取每个人喜欢的数字，我们使用如下代码
#favorite_numbers['xxx']
print("Lxy's favorite number is " + str(favorite_numbers['lxy']) + ".")
print("Lb's favorite number is " + str(favorite_numbers['lb']) + ".")
print("Lm's favorite number is " + str(favorite_numbers['lm']) + ".")
print("Nx's favorite number is " + str(favorite_numbers['nx']) + ".")
print("Cjb's favorite number is " + str(favorite_numbers['cjb']) + ".")

#词汇表
dics = {'list':'列表','var':'变量','int':'整型','boolean':'布尔','str':'字符串'}
print('list' + ':' + (dics['list']))#打印一个词汇，以及含义
print('var' + ':' + (dics['var']))
print('int' + ':' + (dics['int']))
print('boolean' + ':' + (dics['boolean']))
print('str' + ':' + (dics['str']))


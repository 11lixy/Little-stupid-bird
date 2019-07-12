#定义一个名为users的字典，其中包含两个键用户名aeinstein和mcurie，与键相关联的值都是
#一个字典，其中包含用户的名、姓、和居住地
users = {
	'aeinstein':{
	'first':'albert',
	'last':'einstein',
	'location':'princeton',
	},
	'mcurie':{
		'first':'marie',
		'last':'curie',
		'location':'paris',
		},
	}
                              #items() 方法以列表返回可遍历的(键, 值) 元组数组
for username,user_info in users.items():#遍历字典users，依次将每个键存储在变量
#username中，依次将与当前键相关联的字典存储在变量user_info中
	print("\nUsername: " + username)#我们将用户名打印出来
	full_name = user_info ['first'] + "  " + user_info['last']#把内部的字典键存储到变量中
	location = user_info['location']#把内部的字典键存储到变量中

	print("\tFull name: " + full_name.title())
	print("\tLocation: " + location.title())
	

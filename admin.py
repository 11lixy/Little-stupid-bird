user_names = ['admin','l','k','g','i']
if 'admin' in user_names:
#如果用户名为admin，打印一条特殊的问候消息
	print("Hello,admin,would you like to see a status report?")
else:
#否则，打印一条普通的问候消息
	print("Hello,l,thank you for logging in again")
	
#确定列表是不是空的
user_names = []
if user_names:
	for user_name in user_names:
		print("\nHello,everybody")
else:
	print("We need to find some users!")
#使用多个列表	
current_users = ['admin','k','b','z','c']
new_users = ['ADmin','k','g','f','s']
for new_user in new_users:#遍历列表，对于列表的每个元素，我们检查他是否在列表里
	if new_user.lower() in current_users:#检查每个用户名是否被使用，是就打印一
#条消息，指出需要输入别的用户名,加上.lower()使得不区分大小写
		print("需要输入别的用户名")
	else:#否则打印一条消息，指出这个用户名未被使用
		print("用户名未被使用")

#序数习题
numbers = ['1','2','3','4','5','6','7','8','9']
for number in numbers:
	if number == 1:
		print('1st')
	elif number == 2:
		print('2nd')
	elif number == 3:
		print('3rd')
	else:
		print(str(number) + 'th')
		

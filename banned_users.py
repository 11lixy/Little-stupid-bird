banned_users = ['andrew','carolina','advid']
user = 'marie'
if user not in banned_users:#如果user的值未包含在列表banned_users中，python将返回true，进而执行缩进的代码行
	print(user.title() + ",you can post a response if you wish.")

#使用while循环来处理列表和字典

unconfirmed_users = ['alice','brian','candace']#首先，创建一个待验证用户列表
confirmed_usres = []# 和一个用于存储已验证用户的空列表

#验证每个用户，直到没有未验证用户位置
# 将每个经过验证的列表都移到已验证用户列表中
while unconfirmed_users:#循环列表，直到列表变成空的，在这个循环中
    current_user = unconfirmed_users.pop()           #pop()函数以每次一个的方式从列表unconfirmed_users末尾删除为验证的用
    #户，存储到变量current_user中并加入到列表confirmed_users
    print("Verifying user:" + current_user.title())
    confirmed_usres.append(current_user)#append()方法用于将传入的对象附加(添加)到现有列表中

#显示所有已验证的用户
print("\nThe following users have been confirmed:")
for confirmed_usre in confirmed_usres:
    print(confirmed_usre.title())
magicians = ['mayun','wangjianlin','leijun']
for magician in magicians: #for循环魔术师中的名字,从列表取一个名字，存储在变量magician
	print(magician)
	print(magician.title() + ", that was a great trick!")
	print("I can't wait to see your next trick," + magician.title() + ".\n")# "\n" 为换行 
print("Thank you,everyone. That was a great magic show!")#f没有在for循环里面，所以执行一次


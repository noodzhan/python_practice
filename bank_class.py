class Account:
	def __init__(self,name,number,balance):#对象的方法的第一个参数一定是对象本身
	#注意init两边都是两个下滑线
		self.name=name
		self.number=number
		self.balance=balance
	def deposit(self,amount):
		if amount <=0:
			print('存款不得为负')
		else:
			self.balance +=amount
	def withdraw(self,amount):
		if amount >self.balance:
			print('余额不足')
		else:
			self.balance -=amount
	def __str__(self):#返回对象描述字符串
		return "Account({name},{number},{balance})".format(
			name=self.name,number=self.number,balance=self.balance)
    

def account (name,number,balance):
	return {'name': name,'number':number,'balance':balance}
def deposit(acct,amount):
	if amount <=0:
		print('存款不得为负')
	else:
		acct['balance']+=amount
def withdraw(acct,amount):
	if amount>acct['balance']:
		print('余额不足')
	else:
		acct['balance']-=amount
def desc(acct):
	return 'Account:'+ str(acct)
	#'Account:'是str类型就是字符串类型
	#str(acct)也是字符串类型，相同的str类型两者相加
	#返回str类型
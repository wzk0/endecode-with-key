import endecode

def 功能():
	print('''1.加密
		\n2.解密\n''')

def 出结果(结果,标题):
	print('\n')
	print(标题+"的结果如下:")
	print('\n')
	print(结果)
	print('\n')

def 再来一次(文本,密钥,类型):
	选择=input('是/否(y/n)再加/解密一次:')
	if 选择=='y':
		if 类型=='加密':
			程度=input('请输入加密程度:')
			出结果(endecode.加密(文本,密钥,程度),'加密')
		if 类型=='解密':
			次数=input('请输入解密次数:')
			出结果(endecode.解密(文本,密钥,次数),'解密')
		再来一次(文本,密钥,类型)
	else:
		pass


功能()

模式=input('请输入模式:')

if 模式=='1':
	文本=input('请输入待加密文本:')
	密钥=input('请输入密钥:')
	程度=input('请输入加密程度:')
	出结果(endecode.加密(文本,密钥,程度),'加密')
	再来一次(文本,密钥,'加密')

if 模式=='2':
	文本=input('请输入待解密文本:')
	密钥=input('请输入密钥:')
	次数=input('请输入解密次数:')
	出结果(endecode.解密(文本,密钥,次数),'解密')
	再来一次(文本,密钥,'解密')
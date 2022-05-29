import random

##列表化文本

def 列表化(文本):
	列表=[]
	for 字 in list(文本):
		列表.append(字)
	return 列表

##打乱文本形成密钥

def 打乱(文本):
	列表=[]
	for 字 in list(文本):
		列表.append(字)
	random.shuffle(列表)
	return 列表

##合并密钥集

def 合并(文本,程度):
	列表=[]
	零=0
	while 零<=int(程度)-1:
		结果=''.join(打乱(文本))
		列表.append(结果)
		零+=1
	return 列表

##打乱后挑选列表第一项

def 随机(列表):
	random.shuffle(列表)
	return 列表[0]

##加密

def 加密(文本,密钥,程度):
	待插入=合并(密钥,程度)
	列表=列表化(文本)
	长度=len(列表)-1
	数列=list(range(0,长度))
	random.shuffle(数列)
	for 插入物 in 待插入:
		列表.insert(随机(数列),插入物)
	return ''.join(列表)

##解密

def 解密(文本,密钥,次数):
	密钥集=合并(密钥,次数)
	for 可能 in 密钥集:
		文本=文本.replace(可能,'')
	return 文本

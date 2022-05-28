# Python实现的简单的加/解密方法 | 第二弹 | 携带密钥

> 这是我又一次在学校发呆时想出来的加密形式...

## 快速开始

人生苦短，如果你并不想进行开发或了解其它信息，

请直接clone此仓库:

```
git clone https://github.com/wzk0/endecode-with-key.git
```

随后运行`example.py`

![功能图](https://raw.githubusercontent.com/wzk0/photo/main/202205282207052.png)

不过我还是建议你往下看看的！

## 原理

`加密`:打乱原有文字顺序后,随机插入自定义的打乱的不同密钥;

> 总之就是`乱乱乱`.

`解密`:通过密钥的不同组合暴力破解.

## 使用

下载源代码并和你的Python代码放在`同一个文件夹`以调用.

在你的任意同文件夹下的Python代码中输入:

```
import endecode
```

**加密(encode):**

```
result=endecode.加密(文本,密钥,程度)
```

**解密(decode):**

```
result=endecode.解密(文本,密钥,次数)
```

> 加解密中的文本均为`待加解密内容`.

如果你想快速体验,可以`clone`此仓库并运行`example.py`

## 注意

* 密钥的推荐写法:包含原文本中的单字元素,加上一些其他`混淆视听`的单字.例如:

加密`i love you`可使用密钥`ilyf keo`:

> 非元音字母加`eo`等常见字母具有更好的混淆度.

> 空格数量不要过多否则解密爆破的过程`随机性`会大大增高,一般来说`一个空格`足矣.在没有空格的句子中`不应使用`带空格的密钥.(我这里只用了一个空格的密钥,但是爆破次数为10万次)

![效果图](https://raw.githubusercontent.com/wzk0/photo/main/202205282144223.png)

* 并不是加密程度数值越大越好(你需要考虑对方的算力啊!),如下例子:

```
请输入模式:2
请输入待解密文本:etd iusfft sdeiuitdfie us lo iftsdueveuif tdes you
请输入密钥:etdf uis
请输入解密次数:1000000


解密的结果如下:


i love you
```

这是我的一次解密过程,总共爆破了100万次,CPU直接拉满.

## 开发

采用[中文编程](https://github.com/program-in-chinese),代码简洁,~~没~~有~~什么~~注释.
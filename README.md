# sentiment_analysis

1.代码的复用性

1.1.变量和字符串的复用性

一定要注意代码的复用性，如果同一段代码要对不同数据进行操作，那么修改的变量尽量局限在开头一两个，后面的通过调用来修改。
可以通过对变量的统一调用：统一变量 = 特别变量，之后直接调用统一变量即可。
如果是字符串，存储位置：则可以通过“字符串”.format（相应可能修改的变量）来进行调用。
e.g.
# now when I copy the code for another dataset, I can easily change the special name of the dataset for 

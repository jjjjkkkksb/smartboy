def handsome():
	名字=input("你叫个啥?\n")
	print(名字+"是个大帅哥。")
def lian_jia():
	a=int(input("(从1开始)加到几?\n"))
	i=1
	和=0
	while i<=a:
		和=和+i
		i+=1
	print("1+…+%d的和为:"%(a)+str(和))
	
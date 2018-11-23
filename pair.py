import numpy as np
x=[2,2,3,3,3]
result=[]
working_list=[]
def list_reset():
	working_list=[]
	for element in x_l:
		working_list.append(0)
	return working_list
'''
def recur(working_list,carry_point):
	for i in range(0,carry_point):
		working_list[i]=0
	if carry_point<len(working_list):
		working_list[carry_point]+=1
	return working_list
'''

def recur(working_list):
	for i in range(0,len(working_list)-1):
		working_list[i]+=1
		if (working_list[i]>x_l[i]):
			working_list[i]=0
			working_list[i+1]+=1
		if check(working_list)==True:
			return working_list


def check(working_list):
	for i in range(0,len(x_l)):
		if working_list[i]>x_l[i]:
			return False
	return True

def pair_main(x_l_,y_):
	global x_l
	x_l=x_l_
	global y
	y=y_
	working_list=[]
	result=[]
	for i in range(1,(sum(x_l)+1)):
		working_list=list_reset()
		working_list.append(0)
		while working_list[len(x_l)]!=1:
			working_list=recur(working_list)
			if ((sum(working_list)==i)&(working_list[len(x_l)]!=1)):
				temp_res=1
				for j in range(0,len(working_list)-1):
					temp_res=temp_res*pow(y[j],working_list[j])
				result.append(temp_res)
	return result

'''
for i in range(1,(sum(x_l)+1)):
	working_point=0
	working_list=base_list
	while working_point<(len(x_l)):#need changes
		while ((i>=sum(working_list))&(check(working_list)==True)):
			working_list[0]+=1
			if sum(working_list)==i:
				temp_res=1
				print("triggered result")
				print(working_list)
				for j in range(0,len(working_list)):
					temp_res=temp_res*pow(y[j],working_list[j])
				result.append(temp_res)
		carry_point=0
		print("i:")
		print(i)
		for k in range(0,len(working_list)):
			if (working_list[k]>i) | (sum(working_list)>i):
				carry_point+=1
				working_list=recur(working_list,carry_point)
				working_point+=1
print("Result")
print(result)
'''

import numpy as np

def prime_factor(num_x, num_prime):
	pf_x=[]
	pf_x_sum=[]
	for element in num_prime:
		counter=0
		if element>num_x:
			break
		else:
			while True:
				if num_x%element!=0:
					break
				else:
					counter+=1
					pf_x.append(element)
					num_x=num_x/element
			pf_x_sum.append(counter)
	pf_x_sum.append(pf_x)
	return pf_x_sum

def main():
	num_1=int(input("Enter number 1: "))
	num_2=int(input("Enter number 2: "))
	num_lcm=int(input("Enter LCM: "))
	if (num_lcm%num_1!=0) | (num_lcm%num_2!=0):
		print ("The input value is invalid.")
		break
	pf_1=prime_factor(num_1,num_prime)
	pf_2=prime_factor(num_2,num_prime)
	pf_lcm=prime_factor(num_lcm,num_prime)
	#print(list_diff(pf_lcm,pf_1))
	pf_3=[]
	max_length=len(pf_lcm)-1
	for i in range(0,max_length):
		if (pf_lcm[i]>pf_1[i]) & (pf_lcm[i]>pf_2[i]):
			pf_3.append(pf_lcm[i])
		else:
			pf_3.append(0)
	max_component=list(set(pf_lcm[max_length]))
	num_3=1
	for i in range(0,max_length):
		num_3=num_3*pow(max_component[i],pf_3[i])
	print("Value of number 3 is :")
	print(num_3)

num_prime=[2]
non_prime=0
for i in range (3,1000):
	for j in range (2,1000):
		if j>i:
			break
		else:
			if (i!=j) & (i%j==0):
				non_prime=1
				break
	if non_prime==0:
		num_prime.append(i)
	non_prime=0

while True:
	main()
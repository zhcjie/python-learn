def power(x,n):
	s=1
	while n>0:
		n=n-1
		s=s*x
	return s 
x=float(input('x='))
n=float(input('n='))
print('power=',power(x,n))
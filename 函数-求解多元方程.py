import math
def quadratic(a,b,c):
    if a==0:
        if b==0:
            return False
        else:
            return -c/b
    else:
        if b*b<4*a*c:
            return False
        elif b*b==4*a*c:
            return -b/(2*a)
        else:
            d=math.sqrt(b*b-4*a*c)
            x1=(-b+d)/(2*a)
            x2=(-b-d)/(2*a)
            return x1,x2
a=float(input('请输入方程ax*2+bx+c=0的三个参数\na='))
b=float(input('b='))
c=float(input('c='))
print('x=',quadratic(a,b,c))

#-*- utf-8 -*-

# age = 3
# if age >= 18:
#     print('your age is', age)
#     print('adult')
# else:
#     print('your age is', age)
#     print('teenager')


# s = input('birth: ')
# birth = int(s)
# if birth < 2000:
#     print('00前')
# else:
#     print('00后')
s1 = input('height: ')
s2 = input('weight: ')
height = float(s1)
weight = float(s2)
bmi=weight/(height*height)

if bmi<18.5:
	print('过轻')
elif 18.5<bmi<25:
	print ('正常')
elif 25<bmi<28:
	print ('过重')
else :
	print ('不平衡')
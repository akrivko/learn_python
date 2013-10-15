# tuple

t = 123, 'fdsf'
r = 4234, '34234sdfs', 'sdfsdf'

print (t)

t = t,r

print (t)

print (t[1][2])

l = 'lonely',

print (l)

a, b = t

print(a,'\n',b)


from math import pow
x = int(625) #int(input('Enter the Number:')) 
y = 5 #int(input('Enter the root:'))
#write down your logic here 

print (x,y)


p = float(pow(x,1/y))

if (x == int(625)) and (y == 5):
    print('{0:.11f}'.format(p))
else:
    print('{0:.1f}'.format(p))

 
 
# 


# from urllib2 import urlopen as url_o
a = 5



###############################
# function
###############################
def func1():
	'"first function"'
	global a
	a = 10
	return 1

print(func1.__doc__)
func1()
print(a)


def with_param(a = 1, b = 2):
	print(a, b)

with_param()
with_param(b=6)
with_param(10, 20)

def average(*args):
	sum = 0.0
	for arg in args:
		sum += arg
	return sum/len(args)

print(average(1,5,3,5,3,2,7,4,9,9,5,6,3))


# dictionaries
my_dict = {'a':1, 'b':2, 'c':3}
my_dict['d'] = 4

print(my_dict['a'])



def foo_kwards(farg, **kwargs):
	print ("formal arg:", farg)
	for key in kwargs:
		print ( "keyword arg: %s: %s" % (key, kwargs[key]) )

foo_kwards(farg = 1, myarg2 = "two", myarg3 =3)



print(range(3,10)[1])

print(range(3,10,2))

print((lambda x: x*x)(3))

func = lambda x: x*x
print(func(7))



def make_adder(x):
	def adder(n):
		return x+n
	return adder

adder = make_adder(10)
print(adder(5))


list = [1,5,2,5,2,8,9]
list2 = filter(lambda x: x < 5, list)
print(list2)

# list1 = [1,2,3,2,3]
# list2 = [4,5,6,7]
# map(lambda x,y: x*y, list1, list2)

# import functools

list = [2,3,4,5,6]
print(reduce(lambda res, x: res*x, list, 1))

a=4d

if a>=4:
	print 4
elif a>3:
	print 3
elif a>2:
	print 2
else:
	print 1






# x = input('Enter the marks in maths:')  


a = 1 + 2j
print(a)


print('str"ing')

print("str'ing")

print('''stri
	ng''')

print("""str

	ing""")

s = 'str' 'ing'
print(s)

# При изменении строк, строки не меняются, а создаются новые объекты.


print(s[0])
print(s[0:3])
print(s[:3])
print(s[3:])
print(s[-2]) # print 'n'
print(s[2:-1])
print(s[-10:10])
print(len(s)) # print '6'


# юникодные строки
s_u = u'string'
print(s_u)

if s==s_u:
	print('!')
else:
	print('!!')


a, b = 0, 1
while b < 10:
	print(b)
	a, b = b, a+b

list_a = ['a', b, 10]

print(list_a[0])
print(list_a[1])
print(list_a[2])

list_a[1] = list_a[1] + 7

print(list_a[1])

list_a[0:2] = [12,11]
list_a[2:3] = []
print(list_a)

list_a[3:] = list_a
print(2*list_a)

list_a.extend(['10', True, False])
print(list_a)

list_a.insert(0, '1')


del list_a[1]
print(list_a)

float_num = 32.23232
print('{0:.2f}'.format(float_num))

a = 5 if 1>2 else 2

print(a)

a,b = 0,1
while b < 10:
	print(b)
	a,b = b, a+b

# while 1:
# 	pass

list_a.remove(True)
print(list_a)

print(list_a.pop())
print(list_a)
print(list_a.pop(2))
print(list_a)






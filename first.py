print("Hello")

print(10**3)


mylist = []
mylist.append(1)
mylist.append(2)
mylist.append(3)
print(mylist[0]) # prints 1
print(mylist[1]) # prints 2
print(mylist[2]) # prints 3

number = 1 + 2 * 3 / 4.0
print(number)

print(11%3)

even_numbers = [2,4,6,8]
odd_numbers = [1,3,5,7]
all_numbers = odd_numbers + even_numbers
print(' ', all_numbers[3])

name = "John"
age = 23
print ("%s is %d years old." % (name, age))

mylist = [1,2,3]
print ("A list: %s %s" % (mylist, mylist))

data = ("John", "Doe", 53.44)
format_string = "Hello"

print ("%s %s %s. Your current balance is %.2f$." % (format_string,data[0],data[1],data[2]))


a = 1
b = 2
c = 3
a, b, c = b, c, a

print(a,b,c)

def fib():
	f_1 = 1
	f_2 = 1
	yield f_1
	yield f_2
	i=0
	while i<15:
		f_n = f_1 + f_2
		yield f_n
		f_1, f_2 = f_2, f_n
		i = i+1

for i in fib():
	print(i)

sentence = "the quick brown fox jumps over the lazy dog"
words = sentence.split()
print(words)

def foo(first, second, third, *therest):
    print ("First: %s" % first)
    print ("Second: %s" % second)
    print ("Third: %s" % third)
    print ("And all the rest... %s" % list(therest))

foo(1,2,3,4,5,6,7)



def foo(a, b, c, *therest):
    list_n = therest
    return len(list_n)

def bar(a, b, c, **options):
    if options.get("magicnumber") == 7:
        return 1
    else:
    	return bool('false')
    
# test code
if foo(1,2,3,4) == 1:
    print ("Good.")
if foo(1,2,3,4,5) == 2:
    print ("Better.")
if bar(1,2,3,magicnumber = 6) == False:
    print ("Great.")
if bar(1,2,3,magicnumber = 7) == True:
    print ("Awesome!")
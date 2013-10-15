class FirstClass:
	"""First Class"""
	a = 3
	b = 4
	def func1(self):
		return a + b

F_C = FirstClass()

print F_C.a
print FirstClass.__doc__


print bin(12)
print bin(6)

a = 12 & 6
print a

a = 8 << 1
print a


# def main():
#     x = int(input('Enter number:'))
#     menu()
#     ch = int(input('Enter your choice:'))
    
#     while ch in range(1, 3):
#        #Write your code here{ 
#         if ch==1:
#            print (x << 1)
#         elif ch==2:
#             print (x >> 1)
#         elif ch==3:
#             break
        
        
        
#         #}
#         menu()
#         ch = int(input('Enter your choice:'))

# def menu():
#     print("1. Rotate Left\n2. Rotate Right\n3. Exit")

# main()

i = input()

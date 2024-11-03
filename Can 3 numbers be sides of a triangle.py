#Python code that checks if three numbers can be sides of a triangle
print ('Input 3 positive real numbers >0 to check if they can be sides of a triangle')
a=input ('Enter a:')
a=float(a)
b=input ('Enter b:')
b=float(b)
c=input ('Enter c:')
c=float(c)
if a<=0 or b<=0 or c<=0:
    print ('Error-input out of range')
#This is a range check [identified in data dictionary table] that is done to make sure that the input is a positive integer
elif a+b>c and b+c>a and a+c>b:
    print ('These numbers CAN be sides of a triangle')
else:print ('These numbers CANNOT be sides of a triangle')
print ('end')
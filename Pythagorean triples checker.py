#Python code that checks if three numbers can be Pythagorean triples or not
print ('Enter sides a, b, and c to find out if they are Pythagorean triples or not')
a=input ('Enter a:')
a=float(a)
b=input ('Enter b:')
b=float(b)
c=input ('Enter c:')
c=float(c)
if a<=0 or b<=0 or c<=0:
    print ('Error-input out of range')
#This is a range check [identified in data dictionary table] that is done to make sure that the input is a positive integer
elif a**2 + b**2 == c**2:
    print ('They are Pythagorean triples')
else: print ('They are NOT Pythagorean triples')
print ('end')

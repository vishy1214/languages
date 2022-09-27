def squareOf(x):
    print(x*x)

def factorial(x):
    j = 1
    i = 1
    for i in range(x):
        if i > 0:
            j = j * i
    return j

def chainedConditions(x):
    value = 1;
    if(x >= 10):
        if(x == 10):
            value = x * 10
        else:
            value = x * 11
    elif (x >5 and x < 10):
        value = x * x
    else:
        value = x
    return value    

def recursion(n):
    if n <=0 :
        print(' all done')
    else:
        print('~~~~~')
        print(n)
        recursion(n-1)

print("Hello world")
x = 3 * 4

print(x)
squareOf(x)
value = factorial(x)
print(value)
print(chainedConditions(10))
print(chainedConditions(11))
print(chainedConditions(6))
print(chainedConditions(3))
recursion(5)

s = 'hello'
print('String length: ') 
print(len(s))

print('Printing contents of S')
for char in s:
    print(char)
    if char in 'Elegant':
        print(char + ' exists in Elegant')

newString = s + '~Vishwa'

print(newString[0:6])  #hello~
print(newString[5:8])  #~Vi
print(newString[:8])  #hello~Vi
print(newString[3:])  #lo~Vishwa
print(newString[:])   #hello~Vishwa

i = 0
while i < len(s):
    print(i)
    i = i + 1 

word = s 
if word < 'banana':
    print('Your word, ' + word + ', comes before banana.')
elif word > 'banana':
    print('Your word, ' + word + ', comes after banana.')
else:
    print('All right, bananas.')

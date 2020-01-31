# write these lines on python interpreter

5+2
5-2
5*2
5**2    # power
5/2
5.0/2
5.0//2  # integer division
5%2     # remainder

# you can add spaces in between an expression
# a+b ... a + b ... works the same

# what if i wish to share this calculator with my friends
# we need to write these lines on a file
# lets run this file using "python var_op.py"
# there is no output ... what's wrong ??
# when writing on file, we need to tell python whether we wish to see the output or not 

print(5+2)
print(5-2)
print(5*2)
print(5**2)
print(5/2)
print(5.0/2)
print(5.0//2)
print(5%2)

# now what if i want to do these operations with 3 and 4
# and then with 12453 and 738383......will you change the numbers on each line?
# and that too, every time? ... tedious right?
# then lets introduce variables to ease it out

a = 5
b = 2

print(a+b)
print(a-b)
print(a*b)
print(a**b)
print(a/b)
print(a//b)
print(a%b)

# now, just change the values at one place, it will change everywhere
# the operations we learnt above are arithmatic operations
# a combination of these operators follows bodmas
print((3+2)*(2-3))

# there are other operators called comparison operators

print(a==b)
print(a!=b)
print(a>=b)
print(a<=b)
print(a>b)
print(a<b)

# what was the output to the above statements? True/False
# interesting ... lets look into it more deeply
# what do we usually do with True and False? ... Logic Gates !!!

# logical operators ... a = 0 is false(0) ... anything other than that is true(1)

print(a and b)  
print(a or b)   
print(not a)    

# bitwise operator ... assuming you know what binary numbers are

print(a & b)    # find if number is even ... x and 1
print(a | b)    # set any bit to 1
print(a ^ b)    # complement
print(~a)
print(a << b)
print(a >> b)

# what is the difference between OR and | ??
# we will look into it later

# and finally ... identity operator
a=1
b=True
print (a==b)
print (a is b)
a = b
print (a is b)


# but the way these solutions are printed
# doesnt seem very nice, right?
# lets move on to our next module and find out some solution


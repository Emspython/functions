# Do not modify these lines
__winc_id__ = '49bce82ef9cc475ca3146ee15b0259d0'
__human_name__ = 'functions'

# Add your code after this line

#1. greet: takes a name and returns a string in the format:

def greet(name):
    greeting = 'Hello, '
    return f'{greeting}{name}!'

Greets = greet ('Michiel')
print(Greets)

#2. add: takes three numbers (integers or floats) and returns their sum.

def add(a,b,c):
    calculate = (a+b+c)
    return calculate

sum = 5+3+2
print(sum)

#3. positive: takes a number (integer or float) and returns whether or not it is positive in the form of a boolean.
#   You do not have to handle the case where the argument is not an int or a float

def positive(number):
    posnr = number > 0
    return posnr

numb1 = positive (50)
numb2 = positive (-50)
numb3 = positive (0)

print(numb1)
print(numb2)
print(numb3)

#4. negative: takes a number (integer or float)
#  and returns whether or not it is negative in the form of a boolean. 
# You do not have to handle the case where the argument is not an int or float

def negative(number):
    negnumb = number < 0
    return negnumb

numb4 = negative(50)
numb5 = negative(-50)
numb6 = negative(0)

print(numb4)
print(numb5)
print(numb6)


 

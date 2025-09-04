#arithemetic operations on two numbers
def add_nums(a,b):
    return a+b
def sub_nums(a,b):
    return a-b
def multiply_nums(a,b):
    return a*b
def divide(a,b):
    return a/b
def find_remainder(a,b):
    return a%b
def find_pow(a,b):
    return a**b
x=int(input("enter number 1"))
y =int(input("enter numver 2"))
print("sum" ,add_nums(x,y))
print("subract" ,sub_nums(x,y))
print("product",multiply_nums(x,y))
print("division",divide(x,y))
print("remainder",find_remainder(x,y)) 
print("exponent" ,find_pow(x,y))   
def greet():
    print("Hello")
greet()

def add(a,b):
    print(a+b)

add(20,40)

def square(a):
    return a*a

result = square(10)
print(result)

def addition(*numbers):
    print (sum(numbers))
    
addition(10,20,30,40,50,60,70,80,90)

def user(**user):
    print(user)


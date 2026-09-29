# age = input("enter age")
# print(age)
total = 0
numbers={10,20,30,40,50}

for number in numbers:
    total+=number
    
print(total)
    
obj={
    "name":"akash",
    "age":20,
    "clg":"BEC"
}

for key,val in obj.items():
    print(key,val)

for a in range(2): # 0,1
    for b in range(2): #0,1
       for c in range(2):
           print(a,b,c)


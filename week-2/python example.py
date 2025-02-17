#adding two numbers
def sum(a,b):
    return a + b
a=int(input(" "))
b=int(input(" "))
result=sum(a,b)
print(result)


#even numbers from 1 to 20
for i in range(0,21):
    if i%2==0:
        print(i)ss

#largest number in a list
list=[]
for i in range(0,6):
    i=int(input(" "))
    list.append(i)
maximum=max(list)
print(maximum)
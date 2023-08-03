


lst=[]

num=int(input("Enter how many elemnt you want to add in list to sum : "))
for i in range(num):
    ele=int(input("enter elements : "))
    lst.append(ele)

def summ(n):
    sum=0
    for i in n:
        sum+=i
    return sum
print(summ(lst))
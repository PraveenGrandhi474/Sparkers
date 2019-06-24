'''list1=[]
print("Welcome to Regestration")
a=int(input("Please enter number of tickets"))
for i in range(a):
    def name():
        name=input("Enter Name")
        if name.isalpha():
            age()
        else:
            name()
    list1.append(name)
    age=input("Enter Age")
    list1.append(age)
    gender=input("Enter Gender\n1.M(male)\t2.F(female)")
    list1.append(gender)
name()
for i in range(0,a,3):
    print("Name:",end="")
    print(list1[i])
    print("Age:",end="")
    print(list1[i+1])
    print("Gender:",end="")
    print(list1[i+2])'''

list1=[]
print("Welcome to Regestration")
a=int(input("Please enter number of tickets"))
def name():
    n=input("Enter Name")
    if n.isalpha():
        list1.append(n)
        age()
    else:
        print("Wrong Entry")
        name()
def age():
    a=input("Enter Age")
    if a.isdecimal():
        list1.append(a)
        gen()
    else:
        print("Wrong Entry")
        age()
def gen():
    g=input("Enter Gender\n1.M(male)\t2.F(female)\t3.O(Others)")
    if g!='m' or g!='f' or g!='o':
        print("Wrong Entry")
        gen()
    else:
       list1.append(g)
name()
print(list1)
'''
for i in range(a):
    reg()
    print("Ticket%d" %(i+1))
    print("Name:" + list1[i]+ "age")
'''

def reg():
    a=int(input("Enter no of Tickets:"))
    for i in range(1,a):
        z={Name:b,Age:c,Gender:d}
        b=input("Name:")
        c=input("Age:")
        d=input("Gender:")
pnr=int(input("Enter your choice\n1.PNR status\n2.Ticket Regervation\n"))
        

if pnr==1:
    pnr()
elif pnr==2:
    reg()
else:
    print("Invalid selection")

print(z)

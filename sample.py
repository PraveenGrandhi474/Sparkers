import os
f=open("amb.xlsx",'w')
f.write("hiiii.....")
f.close()
f=open("amb.xlsx",'r')
print(f.read())
f.close()
print(os.getcwd())

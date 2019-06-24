import random
import os
str1=''
file_names_list=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
list2=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z',' ']
os.mkdir('F:/asses/a2')
n=random.randint(1,10)
print(n)
for i in range(n):
    b=random.choice(list2)
    list2.remove(b)
    f=open('F:/asses/a2/'+b+'.txt','a')
    for i in range(512):
        str1+=random.choice(file_names_list)
    f.write(str1)
    f.close()
    str1=''
    
    

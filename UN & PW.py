u='abc'
p='xyz'
def un():
    c=input('enter the username:')
    if c==u:
        ps()
    else:
        un()
def ps():
    d=input("enter the password:")
    if d==p:
        print('logged in successfuly')
    else:
        un()

un()

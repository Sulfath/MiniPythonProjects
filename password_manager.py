from cryptography.fernet import Fernet

def loadkey():
    file = open("key.key","rb")
    key = file.read()
    file.close()
    return key

key = loadkey()
fer = Fernet(key)

def add():
  name= input("Account name : ")
  password = input("Password : ")

  with open('password.txt','a') as f:
     f.write(name + "|" + fer.encrypt(password.encode()).decode() + "\n")

'''def write_key():
   key = Fernet.generate_key()
   with open ("key.key","wb") as keyfile:
      keyfile.write(key)'''

#write_key()
def view():
   with open('password.txt','r') as f:
      for line in f.readlines():
         data=line.rstrip()
         user,passw = data.split("|")
         print("User : ",user," | Password : ",fer.decrypt(passw.encode()).decode())

       

while True:

 mode = input("Do you want to add new password or view existing one. Press 'q' to quit?  ").lower()
 
 if mode == 'q':
    break
 if mode == 'add':
    add()
 elif mode == 'view':
    view()
 else:
    print("Invalid Input")
    continue

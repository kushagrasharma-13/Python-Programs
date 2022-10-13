a = 1234
l = 3
while l>0:
  b = int(input("Enter Password: "))
  if b==a:
    print("Login Succesfull")
    break
  else:
    print("Password Incorrect")
    l = l-1
    print("Attempts Left: ",l)
    if(l==0):
      print("Locked Out")

password="mannu"
for i in range(3):
    pwd=input("Enter the password: ")
    j=2
    if(pwd==password):
        print("Welcom")
        break
    else:
        print("Wrong Password Chances Left:",j-i)
        continue
input("press enter to exit")

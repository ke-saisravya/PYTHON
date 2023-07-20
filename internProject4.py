""" Validation of Password """
l,u,n,s = 0,0,0,0
password = input("Enter the password")
upperCase = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
lowerCase = "abcdefghijklmnopqrstuvwxyz"
numbers = "0123456789"
specialChar = "!@#$&()"
uC,lC,nS,sC = [],[],[],[]
if(len(password) >= 8 ):
    for i in password:
        if(i in upperCase):
            u+=1
            uC.append(i)
        elif(i in lowerCase):
            l+=1
            lC.append(i)
        elif(i in numbers):
            n+=1
            nS.append(i)
        elif(i in specialChar):
            s+=1
            sC.append(i)
if(l >= 1 and u >=1 and n >= 1 and s >= 1 and l+u+n+s == len(password)):
    print("UpperCase are",uC,"\nNumber of Uppercase are",u)
    print("LowerCase are",lC,"\nNumber of Lowercase are",l)
    print("Numbers are",nS,"\nNumber of Digits are",n)
    print("SpecialChar are",sC,"\nNumber of SpecialCharacters are",s)
    print("Password Verified")
else:
    print("Invalid Output")

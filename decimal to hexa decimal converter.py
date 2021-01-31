l={10:"A",11:"B",12:"C",13:"D",14:"E",15:"F"}
dec=int(input("Enter number : "))
c=""
while dec>0 :
    a=dec%16
    if a<=15 and a>9 :
        c+=str(l[a])
    else :
        c+=str(a)
    dec//=16
print("dec to hex = ",c[::-1])    

print("welcome to the rollercoster !")
height = int(input("what is ur height "))
age = int(input("what is ur age "))
if height >= 120 :
    print("can ride")
    if age <=12 :
        print("please pay $5")
    elif age >=18 :
        print("please pay $12")
    else :
        print("please pay $7")
else :
    print("cannot ride")
print("welcome to the rollercoatser !")
height = int(input("what is ur height ? \n"))
age = int(input("what is ur age ? \n"))
wants_photo = (input("did u want photo ? take y for yes and n for no \n"))
if height >= 120:
    print("u can ride")
    if age <= 12 :
        bill = 5
        print("pay $5")
    elif age <= 18 :
        bill = 7
        print("pay $7")
    else :
        bill = 12
        print("pay $12")
    if wants_photo =="y" :
        bill += 3
    print(f"final bill ${bill}")
else:
    print("u cannot ride")
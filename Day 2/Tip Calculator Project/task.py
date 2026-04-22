print("welcome to the tip calculator !")
bill = float(input("what was the total bill ?\n"))
tip = int(input("how much tip would you like to give ? 10,12 or 15 ?\n"))
people = int(input("how many people to split the bill ?\n"))
cal = tip / 100 * bill + bill
tol_cal = cal / people
print(f"each person should pay : {tol_cal}")
print(round(tol_cal,2))


# kinda messy but it worked so ¯\_(ツ)_/¯

hours = input("Hours: ")
hrs = float(hours)
payrate = input("Rate: ")
pay = float(payrate)

overtime = 0
ot = float(overtime)

if hrs > 40:
    ot = hrs - 40
    hrs = hrs - ot
    pay = hrs * pay + ot * pay * 1.5
    print("Pay: " + str(pay))
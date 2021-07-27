# ข้อ 17
hour = int(input("hour : "))
minute = int(input("minute : "))
if minute <= 0 or hour <= 0:
  print("please enter positive number")
if minute > 0:
 total = (hour+1)*30
 print(f"car payment time:{total}")

# -------------------------
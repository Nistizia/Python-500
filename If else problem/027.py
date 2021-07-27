# ข้อ 27
isMember = input("Member : ")
bill = float(input("Your bill :"))
if isMember == "yes":
  if bill > 500:
    payment = (bill*95)/100
    print(payment)
  elif bill >1000:
    payment = (bill*90)/100
    print(payment)
  elif bill >5000:
    payment = (bill*85)/100
    print(payment)
if isMember == "No":
  print(f"your payment {bill}")

# -------------------------
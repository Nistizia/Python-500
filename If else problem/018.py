# ข้อ 18
bill = int(input("Enter your bill :"))
hour = int(input("Enter hour :"))
minute = int(input("Enter minute : "))
if minute > 0:
 if bill >=  1000:
   payment = (hour-3)*30
   if payment <= 0:
     print("free parking") 
   else:print(f"Parking fee : {payment}")
  
 else: 
  payment = (hour)*30
  if payment <= 0:
     print("free parking") 
  else: print(f"Parking fee : {payment}")

if minute == 0:
 if bill >=  1000:
   payment = (hour-4)*30
   if payment <= 0:
     print("free parking") 
   else:print(f"Parking fee : {payment}")
  
 else: 
  payment = (hour-1)*30
  if payment <= 0:
     print("free parking") 
  else: print(f"Parking fee : {payment}")
  



# -------------------------
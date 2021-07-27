# ข้อ 29
print("ร้านเรามีไข่เจียว ไข่ดาว ไข่ต้ม"
)
order = input("Menu : ")
amount = int(input("amount : "))
if order == "ไข่ดาว":
  payment = amount*7
  print(f"your bill ไข่ดาว {payment}")
elif order == "ไข่เจียว":
  payment = amount*10
  print(f"your bill ไข่เจียว {payment}")
elif order == "ไข่ต้ม":
  payment = amount*5
  print(f"your bill ไข่ต้ม {payment}")
# -------------------------
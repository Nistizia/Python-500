# ข้อ 24
status = str(input("Enter status: "))
distance = int(input("Enter distance : "))
if status == "good":
  print(f"payment : {distance*10}")
elif status == "normal":
  print(f"payment : {distance*12}")
elif status == "bad":
  print(f"payment : {distance*15}")

# -------------------------
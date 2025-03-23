qtd_km = int(input("type qtd km percorrered: "))
qtd_days = float(input("type qtd days:"))

value_Day = 60 * qtd_days
value_km = 0.15 * qtd_km
total_price = value_Day + value_km

print(f"total: {total_price:5.2f}")

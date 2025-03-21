preco = float(input("type value of merchandising:"))
desc = float(input(" type the discount:"))

Final_value = preco - preco * (desc/100)
print(f"Final value: {Final_value:5.2f} reais")

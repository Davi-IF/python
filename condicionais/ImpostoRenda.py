salary = float(input("type your salary:"))
base = salary
imposto = 0

if base> 3000:
    imposto = imposto + (base - 3000) * 0.35
    
if base > 1000:
    imposto = imposto + (base - 1000) * 0.20
    
print(f"salario: {salary}, imposto: {imposto}")
    

    
    



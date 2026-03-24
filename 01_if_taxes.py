income = float(input("Introduce el ingreso anual: "))

if income <= 85528:
	tax = income * 0.18 - 556.02

else: 
    atax = income - 85528
    atax1 = atax * 0.32
    tax = 14839.02 + atax1

if tax <0:
    tax = 0.0
    
tax = round(tax, 0)
print("El impuesto es:", tax, "pesos")
 
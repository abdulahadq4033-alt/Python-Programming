# Compound Interest program
p=int(input("Enter P: "))
t=int(input("Enter T: "))
r=float(input("Enter R: "))
A=p*(1+r/100)**t
CI=A-p
print(f"Compound Interest: {CI:.2f}")

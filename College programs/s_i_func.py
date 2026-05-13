'''simple interest program using functions'''
def si(p,t,r):
    return (p*t*r)/100
p=float(input("Enter the principle interest: "))
t=float(input("Enter the time: "))
r=float(input("Enter the rate: "))
print(si(p,t,r))

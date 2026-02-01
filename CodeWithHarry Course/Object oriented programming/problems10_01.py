# 1. Create a class “Programmer” for storing information of few programmers
# working at Microsoft.

class programmer:
    company = "Microsoft"
    def __init__(self, name, salary, pincode):
        self.name=name
        self.salary=salary
        self.pincode=pincode

p=programmer("Marcos", 938264, 983421353426)
print(p.name,p.salary,p.pincode, p.company)

r=programmer("Jude Bellingham", 79863287, 4)
print(r.name,r.salary,r.pincode, r.company)
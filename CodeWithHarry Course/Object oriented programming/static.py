class employee:
    lang="py"
    salary=2891482976324986

    def getinfo(self):
        print(f"The language is {self.lang} and salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning world!")
    
marcos=employee()
print(marcos.lang)
employee.getinfo(marcos) 
class employee:
    lang="py"
    salary=2891482976324986

    def getinfo(self):
        print(f"The language is {self.lang} and salary is {self.salary}")
    

marcos = employee()
marcos.lang ="HTML"  # Instance attribute gets more priority than class attribute
print(marcos.lang)
employee.getinfo(marcos) 
''' or we can write marcos.getinfo it is the same'''
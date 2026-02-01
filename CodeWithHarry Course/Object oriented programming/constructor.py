class employee:
    lang="py"
    salary=2891482976324986

    def __init__(self, name, lang, salary):
        self.name=name
        self.lang=lang
        self.salary=salary
        print("I am creating an object")
    def getinfo(self):
        print(f"The language is {self.lang} and salary is {self.salary}")
    @staticmethod
    def greet():
        print("Good morning world!")
    
marcos=employee("Marcos Rafinho", "HTML and CSS", 89326478)
print(marcos.name, marcos.lang, marcos.salary)

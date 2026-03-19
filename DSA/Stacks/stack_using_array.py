class stack:
    def __init__(self):
        self.stack=[]
    
    def push(self,item):
        self.stack.append(item)
        print(item,"pushed to stack")
    def pop(self):
        if len(self.stack)==0:
            print("Stack underflow")
        else:
            print(self.stack.pop(),"popped from stack")

    def peek(self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            print("Top element: ", self.stack[-1])
        
    def display(self):
        if len(self.stack)==0:
            print("Stack is empty")
        else:
            print("Stack elements: ",self.stack)

s=stack()
s.push(20)
s.push(30)
s.push(45)
s.peek()
s.display()
s.pop()
s.push(58)
s.display()
# initiate a class

class employee:
    #special_method/magic_method/dunder_method/constructor/initializer
    def __init__(self):
        print("started exceution of attribute/constructor")
        self.id=101
        self.salary=50000
        self.designation="developer"
        print("completed exceution of attribute/constructor")

    def travel(self,destination):
        print("started exceution of method travel manually")
        print(f"employee is now travelling to {destination}")

# create object/instance of class
sam=employee()

# print(sam.id)
# print(sam.salary)
# print(sam.designation)


sam.travel("bangalore")
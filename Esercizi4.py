class Cat():
    razza="felino"
    def __init__(self, name, age):
        self.name=name
        self.age=age
siamese=Cat("Luna", "4")
print(siamese.name)
siamese.name="Milù"
print(siamese.name)
print(siamese.age)
print(siamese.razza)
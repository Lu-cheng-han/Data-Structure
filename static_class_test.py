


class Hank:
    name :str = "hank"
    age :int = 24 
    

    @classmethod
    def get_age(cls):
        return cls.age
    
    @classmethod
    def add_age(cls):
        cls.age += 1

    @staticmethod
    def add(a,b):
        return a+b
    
Hank.add_age()
a = Hank()
b = Hank()
print("a",id(a),"b",id(b))
print(id(a.age))
print(id(b.age))
print(id(Hank.age))
print(id(Hank.get_age()))
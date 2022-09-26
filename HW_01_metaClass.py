class Meta(type):
    children_number = 0
    def __new__(mcs, name, bases, dict):
        print(f'{mcs} __new__ Metaclass called')
        dict["class_number"] = Meta.children_number
        Meta.children_number = Meta.children_number + 1
        return super().__new__(mcs, name, bases, dict)
       

    @classmethod
    def __prepare__(mcs, name, bases, **kwargs):
        print(f'{mcs} __prepare__ Metaclass called')
        return super().__prepare__(name, bases, **kwargs)

    def __call__(cls, *args, **kwargs):
        print(f'{cls} __call__ Metaclass called')
        return super().__call__(*args, **kwargs)


Meta.children_number = 0


class Cls1(metaclass=Meta):
    def __init__(self, data):
        print(f'{self}, __init__ Cls1 called')
        self.data = data


class Cls2(metaclass=Meta):
    def __init__(self, data):
        print(f'{self}, __init__ Cls2 called')
        self.data = data


print("Cls1.class_number = ", Cls1.class_number)
print("Cls2.class_number = ", Cls2.class_number)


assert (Cls1.class_number, Cls2.class_number) == (0, 1)
a, b = Cls1(''), Cls2('')
assert (a.class_number, b.class_number) == (0, 1)



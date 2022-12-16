class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print("Object is being deconstructed!")


p = Person("Harvey", 27)


class Vector:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    # Overriding addition function
    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __repr__(self):
        # How to represent the Vector when we need it
        return f"X: {self.x}, Y: {self.y}"

    # def __str__(self):
    #     # What happens when is type cast the Vector into sting.
    #     return "This is a vector!"

    def __len__(self):
        return 10

    def __call__(self, *args, **kwargs):
        print("Hello, I was called!")


v1 = Vector(10, 20)
v2 = Vector(50, 60)

# We need the definition of the addition
# TypeError: unsupported operand type(s) for +: 'Vector' and 'Vector'
v3 = v1 + v2

print(v3)
print(v3.x)
print(v3.y)


print(f"Len: {len(v3)}")

v3()

# MRO — Method Resolution Order
# diamond problem, or even the deadly diamond of death

class A:
    def info(self):
        print('Class A')

class B(A):
    def info(self):
        print('Class B')

class C(A):
    def info(self):
        print('Class C')

class D(B, C):
    pass

D().info() # D has no info method, so it starts looking for left to right in superclasses (B, C), and then up to hierarchy (A)

# class D(A, C): TypeError: Cannot create a consistent method resolution order (MRO) for bases A, C - cannnot use supersuperclass and superclass

# polymorphism is used when different class objects share conceptually similar methods (but are not always inherited)
# polymorphism leverages clarity and expressiveness of the application design and development;
# when polymorphism is assumed, it is wise to handle exceptions that could pop up.
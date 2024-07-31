class MyClass:
    def __init__(self, c):
        self._c = c

    def get_c(self):
        return self._c

# Usage:
obj = MyClass(42)
print(obj.get_c())  # Outputs: 42

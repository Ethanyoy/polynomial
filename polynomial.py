class X:
    def __repr__(self):
        return "X"

    def evaluate(self, num):
        return num

class Int:
    def __init__(self, i):
        self.i = i
    
    def __repr__(self):
        return str(self.i)

    def evaluate(self, num):
        return self.i

class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
    
    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)

    def evaluate(self, num):
        return self.p1.evaluate(num) + self.p2.evaluate(num)

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " - " + repr(self.p2)

    def evaluate(self, num):
        return self.p1.evaluate(num) - self.p2.evaluate(num)

class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub)):
            p1_repr = f"( {repr(self.p1)} )"
        else:
            p1_repr = repr(self.p1)
        
        if isinstance(self.p2, (Add, Sub)):
            p2_repr = f"( {repr(self.p2)} )"
        else:
            p2_repr = repr(self.p2)

        return f"{p1_repr} * {p2_repr}"

    def evaluate(self, num):
        return self.p1.evaluate(num) * self.p2.evaluate(num)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, (Add, Sub)):
            p1_repr = f"( {repr(self.p1)} )"
        else:
            p1_repr = repr(self.p1)
        
        if isinstance(self.p2, (Add, Sub)):
            p2_repr = f"( {repr(self.p2)} )"
        else:
            p2_repr = repr(self.p2)

        return f"{p1_repr} / {p2_repr}"

    def evaluate(self, num):
        return self.p1.evaluate(num) / self.p2.evaluate(num)


poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly)  # Expected output: 4 + 3 + X + 1 * (X * X + 1)
print(poly.evaluate(-1))  # Expected numerical output for X = -1

poly1 = Mul(X(), Add(Int(1), Int(3)))
print(poly1)  # Expected output: X * (1 + 3)
print(poly1.evaluate(-2))  # Expected numerical output for X = -2


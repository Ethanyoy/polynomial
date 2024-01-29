class X:
    def __init__(self):
        pass

    def __repr__(self):
        return "X"


class Int:
    def __init__(self, i):
        self.i = i

    def __repr__(self):
        return str(self.i)


class Add:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return repr(self.p1) + " + " + repr(self.p2)


class Mul:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        if isinstance(self.p1, Add):
            if isinstance(self.p2, Add):
                return "( " + repr(self.p1) + " ) * ( " + repr(self.p2) + " )"
            return "( " + repr(self.p1) + " ) * " + repr(self.p2)
        if isinstance(self.p2, Add):
            return repr(self.p1) + " * ( " + repr(self.p2) + " )"
        return repr(self.p1) + " * " + repr(self.p2)

class Div:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"({repr(self.p1)}) / ({repr(self.p2)})"

class Sub:
    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def __repr__(self):
        return f"({repr(self.p1)}) - ({repr(self.p2)})"

poly = Add(Add(Int(4), Int(3)), Add(X(), Mul(Int(1), Add(Mul(X(), X()), Int(1)))))
print(poly)

print(Sub(Int(5), Int(3)))          # Expected: (5) - (3)
print(Sub(X(), Int(2)))             # Expected: (X) - (2)
print(Sub(Add(X(), Int(1)), Int(4)))# Expected: ((X) + (1)) - (4)

print(Div(Int(10), Int(2)))         # Expected: (10) / (2)
print(Div(X(), Int(5)))             # Expected: (X) / (5)
print(Div(Mul(X(), Int(3)), X()))   # Expected: ((X) * (3)) / (X)


print(Add(Div(X(), Int(2)), Sub(X(), Int(3)))) # Expected: ((X) / (2)) + ((X) - (3))

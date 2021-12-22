from math import floor, ceil


class Number:
    def __str__(self):
        return f"[{self.x},{self.y}]"

    def __init__(self):
        self.parent = None
        self.parent_position = None
        self.x = None
        self.y = None

    def next_digit(self):
        node = self
        while node.parent_position == "y":
            node = node.parent
        if node.parent_position is None:
            return None, None, None
        node = node.parent
        if not isinstance(node.y, Number):
            return node, "y", node.y
        node = node.y
        while isinstance(node.x, Number):
            node = node.x
        return node, "x", node.x
   
    def previous_digit(self):
        node = self
        while node.parent_position == "x":
            node = node.parent
        if node.parent_position is None:
            return None, None, None
        node = node.parent
        if not isinstance(node.x, Number):
            return node, "x", node.x
        node = node.x
        while isinstance(node.y, Number):
            node = node.y
        return node, "y", node.y


    def explode(self, level=0):
        exploded = False
        if level >= 4 and isinstance(self.x,int) and isinstance(self.y,int):
            print("exploding", self)
            number, position, current = self.next_digit()
            if current is not None:
                setattr(number, position, current + self.y)
            number, position, current = self.previous_digit()
            if current is not None:
                setattr(number, position, current + self.x)
            setattr(self.parent, self.parent_position, 0)
            return True
        else:
            if isinstance(self.x, Number):
                exploded = self.x.explode(level+1) or exploded
            if isinstance(self.y, Number):
                exploded = self.y.explode(level+1) or exploded
        return exploded
    
    def split(self):
        splitted = False
        if isinstance(self.x, Number):
            splitted = self.x.split() or splitted
        elif self.x >= 10:
            n = Number()
            n.x = floor(self.x/2)
            n.y = ceil (self.x/2)
            n.parent_position = "x"
            n.parent = self
            self.x = n
            splitted = True
        if isinstance(self.y, Number):
            splitted = self.y.split() or splitted
        elif self.y >= 10:
            n = Number()
            n.x = floor(self.y/2)
            n.y = ceil (self.y/2)
            n.parent_position = "y"
            n.parent = self
            self.y = n
            splitted = True
        return splitted

    def __add__(self, other):
        return Number.parse(f"[{self},{other}]")

    @staticmethod
    def parse(value):
        position = "x"
        current = None
        for (i, d) in enumerate(value):
            if d == "[":
                if current is not None:
                    inner = Number()
                    setattr(current, position, inner)
                    inner.parent = current
                    inner.parent_position = position
                    current = inner
                else:
                    current = Number()
                position = "x"
            elif d == "]":
                position = "x"
                current = current.parent if current.parent is not None else current
            elif d == ",":
                position = "y"
            elif str.isdigit(d):
                v = int(value[i-1:i+1]) if str.isdigit(value[i-1]) else int(d)
                setattr(current, position, v)

        if current is not None:
            current.simplify()            
        return current
    
    def simplify(self):
        print(self)
        simplified = False
        while self.explode():
            print("explode", self)
            simplified = True
        while self.split():
            print("split", self)
            simplified = True
        if simplified:
            self.simplify()

def add_sequence(sequence):
    numbers = tuple(map(Number.parse, sequence))
    acu = numbers[0]
    for i in range(1, len(numbers)):
        acu = acu + numbers[i]
    return acu

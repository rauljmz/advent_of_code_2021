from math import fabs, floor, ceil


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

    def get_level(self, level):
        if isinstance(self.x, int) and isinstance(self.y, int) and level <= 0:
            return self
        if isinstance(self.x, Number):
            child_node = self.x.get_level(level-1)
            if child_node is not None:
                 return child_node
        
        if isinstance(self.y, Number):
            child_node = self.y.get_level(level-1)
            if child_node is not None:
                 return child_node
        return None

    def get_first_two_digit_value(self):
        if isinstance(self.x, int) and self.x >= 10:
            return self, "x", self.x
        if isinstance(self.y, int) and self.y >= 10:
            return self, "y", self.y
        if isinstance(self.x, Number):
            node, position, value = self.x.get_first_two_digit_value()
            if node:
                return node, position, value
        if isinstance(self.y, Number):
            node, position, value = self.y.get_first_two_digit_value()
            if node:
                return node, position, value
        return None, None, None

    def explode(self):
        node_to_explode = self.get_level(4)
        if node_to_explode is not None:        
            print("exploding", node_to_explode)
            number, position, current = node_to_explode.next_digit()
            if current is not None:
                setattr(number, position, current + node_to_explode.y)
            number, position, current = node_to_explode.previous_digit()
            if current is not None:
                setattr(number, position, current + node_to_explode.x)
            setattr(node_to_explode.parent, node_to_explode.parent_position, 0)
            return True
        return False
    
    def split(self):
        node_to_split, position, value = self.get_first_two_digit_value()
        if node_to_split is not None:
            n = Number()
            n.x = floor(value/2)
            n.y = ceil (value/2)
            n.parent_position = position
            n.parent = node_to_split
            setattr(node_to_split, position, n)
            return True
        return False

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
        exploded = False
        while self.explode():
            print("explode", self)
            exploded = True
        if self.split() or exploded:
            self.simplify()

def add_sequence(sequence):
    numbers = tuple(map(Number.parse, sequence))
    acu = numbers[0]
    for i in range(1, len(numbers)):
        acu = acu + numbers[i]
    return acu

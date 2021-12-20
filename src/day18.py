class Symbol:
    def __init__(self, value, previous):
        self.value = value
        self.previous = previous
        self.next = None
        if previous is not None:
            previous.set_next(self)

    def set_next(self, next):
        self.next = next
        
    def __str__(self):
        return self.value

    @staticmethod
    def build(value, previousvalue):
        mapping = {
            "[": BracketOpen,
            "]": BracketClose,
            ",": Separator,
        }
        if value in mapping:
            return mapping[value](previousvalue)
        else:
            return Symbol(value, previousvalue)

class BracketOpen(Symbol):
    def __init__(self, previous):
        super().__init__("[", previous)

class BracketClose(Symbol):
    def __init__(self, previous):
        super().__init__("]", previous)

class Separator(Symbol):
    def __init__(self, previous):
        super().__init__(",", previous)

class Digit(Symbol):
    def __init__(self, value, previous):
        super().__init__(value, previous)


class Number:
    def __init__(self, representation):
        symbols = []
        for symbol in representation:
            symbols.append(
                Symbol.build(symbol, symbols[-1] if len(symbols) > 0 else None)
                )
        self.first_symbol = symbols[0]

    def explode(self):
        pass

    def __iter__(self):
        self.current = self.first_symbol
        return self

    def __next__(self):
        if self.current:
            tmp = self.current
            self.current = self.current.next
            return tmp
        else:
            raise StopIteration

    def __str__(self):
        return "".join(map(str,self))
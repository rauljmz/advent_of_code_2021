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
            return Digit(value, previousvalue)


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
        super().__init__(int(value), previous)
    
    def __str__(self):
        return str(self.value)


class Number:
    def __init__(self, representation):
        symbols = []
        for symbol in representation:
            symbols.append(
                Symbol.build(symbol, symbols[-1] if len(symbols) > 0 else None)
            )
        self.first_symbol = symbols[0]

    def explode(self):
        depth = 0
        symbol = self.first_symbol
        while depth < 5 or not isinstance(symbol, Digit):
            if isinstance(symbol, BracketOpen):
                lastOpen = symbol
                depth += 1
            elif isinstance(symbol, BracketClose):
                depth -= 1
            symbol = symbol.next
        if symbol:
            value = symbol.value
            prev_symbol = symbol.previous
            while not isinstance(prev_symbol, Digit) and prev_symbol:
                prev_symbol = prev_symbol.previous
            if prev_symbol:
                prev_symbol.value += value
            
            value = symbol.next.next.value
            next_symbol = symbol.next.next.next
            while not isinstance(next_symbol, Digit) and next_symbol:
                next_symbol = next_symbol.next
            if next_symbol:
                next_symbol.value += value
            close = symbol.next.next.next
            zero = Digit(0,lastOpen.previous)
            zero.set_next(close.next)

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
        return "".join(map(str, self))

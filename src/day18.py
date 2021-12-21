from math import floor, ceil

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
            if isinstance(previousvalue, Digit):
                previousvalue.value = previousvalue.value*10 + int(value)
                return previousvalue
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
        while symbol is not None and (depth < 5 or not isinstance(symbol, Digit)):
            if isinstance(symbol, BracketOpen):
                lastOpen = symbol
                depth += 1
            elif isinstance(symbol, BracketClose):
                depth -= 1
            symbol = symbol.next if symbol else None
        if symbol is not None:
            print(self)
            print(f'exploding at {symbol}')
            value = symbol.value
            prev_symbol = symbol.previous
            while not isinstance(prev_symbol, Digit) and prev_symbol is not None:
                prev_symbol = prev_symbol.previous
            if prev_symbol is not None:
                prev_symbol.value += value
            value = symbol.next.next.value
            next_symbol = symbol.next.next.next
            while not isinstance(next_symbol, Digit) and next_symbol is not None:
                next_symbol = next_symbol.next
            if next_symbol is not None:
                next_symbol.value += value
            close = symbol.next.next.next
            zero = Digit(0,lastOpen.previous)
            zero.set_next(close.next)
            close.previous = zero
            self.explode()

    def split(self):
        done = False
        for symbol in self:
            if isinstance(symbol, Digit) and (symbol.value >= 10):
                print(self)
                print(f'splitting at {symbol}')
                open = BracketOpen(symbol.previous)
                x = Digit(floor(symbol.value / 2),open)
                sep = Separator(x)
                y = Digit(ceil(symbol.value / 2), sep)
                close = BracketClose(y)
                close.set_next(symbol.next)
                symbol.next.previous = close
                done = True
        return done
            

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

    def __add__(self, other):
        result = Number(f"[{self},{other}]")
        result.explode()
        while result.split():
            result.explode()
        # print(result)
        return result

def add_sequence(sequence):
    numbers = tuple(map(Number, sequence))
    acu = numbers[0]
    for i in range(1, len(numbers)):
        acu = acu + numbers[i]
    return acu
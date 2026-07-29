class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x: int) -> None:
        self.input.append(x)

    def pop(self) -> int:
        self._transfer()
        return self.output.pop()

    def peek(self) -> int:
        self._transfer()
        return self.output[-1]

    def empty(self) -> bool:
        return not self.input and not self.output

    def _transfer(self) -> None:
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
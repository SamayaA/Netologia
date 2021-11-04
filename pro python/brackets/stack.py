from typing import Any


class stack:
    def __init__(self) -> None:
        self.st = list()
    
    def is_empty(self) -> bool:
        return not len(self.st)
    
    def push(self, item) -> None:
        self.st.append(item)

    def pop(self):
        return self.st.pop()

    def peek(self):
        if self.size() > 0:
            return self.st[-1]

    def size(self) -> int:
        return len(self.st)
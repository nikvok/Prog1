from functools import total_ordering


class finance:
    nev: str
    jel: str
    __ar: int

    def __init__(self, nev: str, jel: str, ar: int) -> None:
        self.nev = nev
        self.jel = jel
        self.__ar = ar

    def __repr__(self) -> str:
        return f"finance({self.nev} {self.jel} {self.__ar}"

    def __str__(self) -> str:
        return f"#{self.nev} ({self.valuta}): {self.__ar} "

    def __eq__(self, o: object) -> bool:
        if not isinstance(o, finance):
            return False
        return (self.nev, self.jel, self.__ar) == (o.nev, o.jel, o.__ar)

    def __lt__(self, other):
        if not isinstance(other, finance):
            return NotImplemented
        return (-self.__ar, self.nev, self.jel)


class kripto(finance):
    __tnev = str

    def __init__(self, nev: str, jel: str, ar: int, tnev=str) -> None:
        super().__init__(nev, jel, ar)
        self.__tnev == tnev

    def tervezoneve(self):
        return self.__tnev
    def tervenzonev(self, value):
        return self.__tnev == value

    def __repr__(self) -> str:
        return f"({self.nev}, self.jel, {self.__ar}, {self.__tnev})"

    def __str__(self) -> str:
        return f"{self.jel} ({self.nev}): ${self.__ar}, @{self.__tnev}"


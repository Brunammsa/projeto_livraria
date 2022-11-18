from functions.helpers import real_float_to_str


class Book:
    count = 1

    def __init__(
        self: object, title: str, author: str, pages: int, price: float
    ) -> None:
        self.__code: int = Book.count
        self.__title: str = title
        self.__author: str = author
        self.__pages: int = pages
        self.__price: float = price

        Book.count += 1

    @property
    def code(self: object) -> int:
        return self.__code

    @property
    def title(self: object) -> str:
        return self.__title

    @property
    def author(self: object) -> str:
        return self.__author

    @property
    def pages(self: object) -> int:
        return self.__pages

    @property
    def price(self: object) -> float:
        return self.__price

    def __str__(self) -> str:
        return f'Código: {self.code}\nTítulo: {self.title}\nAutor: {self.author}\nNúmero de Páginas: {self.pages}\nPreço: {real_float_to_str(self.price)}'

from typing import List, Dict
from time import sleep

from functions.product import Book
from functions.helpers import real_float_to_str

books: List[Book] = []
shop: List[Dict[Book, int]] = []


def main() -> None:
    menu()


def menu() -> None:
    print('~~~~~~~~~~~~~~~~~~ Bem Vindo(a) a livraria ~~~~~~~~~~~~~~~~~~')
    print('~~~~~~~~~~~~~~~~~~~~~~  Nuxa BookShop  ~~~~~~~~~~~~~~~~~~~~\n\n')
    print('Selecione uma das opções abaixo:\n')
    print(
        '1- Cadastrar produto\n2- Listar Livro\n3- Comprar livro\n4- Visualizar Carrinho\n5- Fechar pedido\n6- fechar o sistema'
    )

    option: int = int(input())

    if option == 1:
        register_book()

    elif option == 2:
        list_book()

    elif option == 3:
        buy_book()

    elif option == 4:
        view_cart()

    elif option == 5:
        close_order()

    elif option == 6:
        print('Volte sempre!')
        sleep(2)
        exit(0)
    else:
        print('Opção inválida')
        sleep(1)
        menu()


def register_book() -> None:
    print('Cadastro do livro')
    print('~~~~~~~~~~~~~~~~~\n')

    title: str = input('Informe o títlo do livro: ')
    author: str = input('Informe o autor do livro: ')
    pages: int = int(input('Informe a quantidade de páginas do livro: '))
    price: float = float(input('Informe o preço do livro: '))

    book: Book = Book(title, author, pages, price)

    books.append(book)

    print(f'O livro {book.title} foi cadastrado com sucesso!')
    sleep(2)
    menu()


def list_book() -> None:
    if len(books) > 0:
        print('Listagem de livros')
        print('~~~~~~~~~~~~~~~~~~')

        for book in books:
            print(book)
            print('-------------------------------')
            sleep(1)
    else:
        print('Ainda não existem livros cadastrados')
    sleep(2)
    menu()


def buy_book() -> None:
    if len(books) > 0:
        print('Informe o código do livro que deseja adicionar ao carrinho')
        print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        print('-------------------- Livros disponíveis ------------------\n')

        for book in books:
            print(book)
            print('---------------')
            sleep(1)

        code: int = int(input())

        book: Book = get_book_by_code(code)

        if book:
            if len(shop) > 0:
                shop_check: bool = False
                for item in shop:
                    quant: int = item.get(book)
                    if quant:
                        item[book] = quant + 1
                        print(
                            f'O {book.title} agora possui {quant + 1} unidades no carrinho'
                        )
                        shop_check = True
                        sleep(2)
                        menu()
                if not shop_check:
                    book_dict = {book: 1}
                    shop.append(book_dict)
                    print(f'O livro {book.title} foi adicionado ao carrinho')
                    sleep(2)
                    menu()

            else:
                item = {book: 1}
                shop.append(item)
                print(f'O livro {book.title} foi adicionado ao carrinho')
                sleep(2)
                menu()
        else:
            print(f'O livro com o código {code} não foi encontrado')
            sleep(2)
            menu()

    else:
        print('Ainda não existem livros no carrinho')
        sleep(2)
        menu()


def view_cart() -> None:
    if len(shop) > 0:
        print('Livros no carrinho')

        for item in shop:
            for datas in item.items():
                print(datas[0])
                print(f'Quantidades: {datas[1]}')
                print('------------------------------')
                sleep(1)

    else:
        print('Ainda não existem livros no carrinho')
    sleep(2)
    menu()


def close_order() -> None:
    if len(shop) > 0:
        total_value: float = 0

        print('Livros do carrinho')
        for item in shop:
            for datas in item.items():
                print(datas[0])
                print(f'Quantidade: {datas[1]}')
                total_value += datas[0].price * datas[1]
                print('-------------------------------')
                sleep(1)

        print(f'Sua fatura é de {real_float_to_str(total_value)}')
        print('Volte sempre!')
        shop.clear()
        sleep(5)
    else:
        print('Ainda não existem livros no carrinho')
        sleep(2)
        menu()


def get_book_by_code(code: int) -> Book:
    p: Book = None

    for book in books:
        if book.code == code:
            p = book

    return p


if __name__ == '__main__':
    main()

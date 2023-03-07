def build_matryoshka(size, n):
    if n >= 1:
        print(f"Создаём низ матрёшки размера {size}.")
        print(f'n:{n}')
        build_matryoshka(size - 1, n - 1)
        print(f"Создаём верх матрешки размера {size}.")
        print(f'n:{n}')
    else:
        return


build_matryoshka(5, 3)

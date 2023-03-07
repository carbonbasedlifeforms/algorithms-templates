def stairs_builder(n):
    if n == 0:
        return
    print(f"Осталось построить {n} ступеней.")
    stairs_builder(n - 1)


stairs_builder(10)

year = int(input("Введите год: "))

if year % 4 == 0 & (year % 100) % 4 == 0:
    print("Год " + str(year) + " високосный")
else:
    print("Год " + str(year) + " не високосный")
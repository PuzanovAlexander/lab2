count = int(input("Введите количество слов: "))
line = []
n = 0

while i < count :
    word = input("Введите слово " + str(n + 1) + ': ')
    line.append(word)
    n += 1

print(" ".join(line))
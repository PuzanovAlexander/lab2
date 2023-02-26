count = int(input("Введите количество слов: "))
line = []
i = 0

while i < count :
    word = input("Введите слово " + str(i + 1) + ': ')
    line.append(word)
    i += 1

print(" ".join(line))
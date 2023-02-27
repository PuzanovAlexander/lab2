firstcolor = str(input("Введите первый цвет:")) 
secondcolor = str(input("Введите второй цвет:"))

if (firstcolor == "красный" or secondcolor == "красный") and (firstcolor == "синий" or secondcolor == "синий"):
    print("фиолетовый")
elif (firstcolor == "красный" or secondcolor == "красный") and (firstcolor == "жёлтый" or secondcolor == "жёлтый"):
    print("оранжевый")
elif (firstcolor == "синий" or secondcolor == "синий") and (firstcolor == "жёлтый" or secondcolor == "жёлтый"):
    print("зелёный")
elif firstcolor == secondcolor and (firstcolor == "красный" or firstcolor == "синий" or firstcolor == "жёлтый"):
    print("Ошибка цвета, введены одинаковые цвета")
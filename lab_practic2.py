a=int(input("Введите номер места:"))
if a>0 and a<37:
    print ("купе")
else:
    print ("боковое место")
if a%2==0:
    print("вехняя полка")
else:
    print("нижняя полка")
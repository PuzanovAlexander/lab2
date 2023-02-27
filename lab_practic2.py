place=int(input("Введите номер места:"))
# области определения для места
if place>=1 and place<=36:
    print ("купе")
elif place>=37 and place<=54:
    print ("боковое место")
if place<=54 and place%2==0:
    print("вехняя полка")
elif place<=54 and place%2==1:
    print("нижняя полка")
#верхний и нижний порог значения места вагона    
if place>=55:
    print ('такого места нет в вагоне')
elif place<=0:
    print ('такого места нет в вагоне')
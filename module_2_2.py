first = int(input("первое число "))
second = int(input("второе число "))
third = int(input("третье число "))
if first == second != third or first != second == third or first == third != second :
    print(2)
elif first == second == third :
    print(3)
elif first != second != third:     # или else
    print(0)
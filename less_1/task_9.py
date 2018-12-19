print("Введите три числа")
a = int(input("Введите первое число: "))
b = int(input("Введите второе число: "))
c = int(input("Введите третье число: "))

if a < b < c or a > b > c:
    print(f"{b} - среднее число")
elif b < a < c or b > a > c:
    print(f"{a} - среднее число")
else:
    print(f"{c} - среднее число")

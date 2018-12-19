a = int(input("Введите год: "))

if a % 4 != 0:
    print(f"{a} - невисикосный год")
elif a % 100 == 0:
    if a % 400 == 0:
        print(f"{a} - висикосный год")
    else:
        print(f"{a} - невисикосный год")
else:
    print(f"{a} - висикосный год")
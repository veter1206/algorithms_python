a = 1
l = int(input("Номер буквы в алфавите: "))
a = a - ord("a") + 1
l = ord("a") + l - 1
print("Это буква", chr(l))
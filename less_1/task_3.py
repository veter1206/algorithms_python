print("Введите координаты первой точки(x1;y1):")
x1 = float(input("x1 = "))
y1 = float(input("y1 = "))

print("Введите координаты второй точки(x2;y2):")
x2 = float(input("x2 = "))
y2 = float(input("y2 = "))

k = (y1 - y2) / (x1 - x2)
b = y2 - k * x2
print(f"y = {k} * x + {b}")
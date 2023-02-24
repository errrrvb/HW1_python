x1 = int(input("x1: "))
y1 = int(input("y1: "))
x2 = int(input("x2: "))
y2 = int(input("y2: "))

if x1 > 0 and x2 > 0: # определяем по x - 1 или 4 четверть
    if y1 > 0 and y2 > 0 or y1 < 0 and y2 < 0: # проверяем, находятся ли точки по y в одной четверти (в первой или четвертой)
        print("YES")
    else:
        print("NO")
elif x1 < 0 and x2 < 0: # значит, у нас 2 или 3 четверти по x
    if y1 > 0 and y2 > 0 or y1 < 0 and y2 < 0: # проверяем, находятся ли точки по y в одной четверти (во второй или третьей)
        print("YES")
    else:
        print("NO")
else:
    print("NO")


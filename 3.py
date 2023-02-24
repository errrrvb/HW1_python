n = int(input())                           # код получился достаточно большим, так как много действий тут повторяются
if n >= 60:                                # главное, что он работает
    a = n % 60
    if a == 0:
        print(f"0 0 {n//60}")
    elif n % 10 == 9:
        n += 1
        if n % 60 == 0:
            print(f"0 0 {n//60}")
        else:
            a = n % 60
            b = a % 10
            a -= b
            print(f"{b//1} {a//10} {n//60}")
    else:
        b = a % 10
        a -= b
        print(f"{b//1} {a//10} {n//60}")
else:
    if n % 10 == 0:
        print(f"0 {n//10} {0}")
    elif n % 10 == 9:
        n += 1
        if n == 60:
            print(f"0 0 {n//60}")
        elif n % 10 == 0:
            print(f"0 {n//10} 0") 
    else:
        a = n % 10
        b = n - a
        print(f"{a//1} {b//10} 0")
    
    
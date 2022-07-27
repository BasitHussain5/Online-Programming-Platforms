while True:
    fuel = input("Fraction: ")
    try:
        nume, demo = fuel.split("/")
        new_nume = int(nume)
        new_demo = int(demo)
        
        f = new_nume / new_demo
        if f <= 1:
            break
    except (ValueError, ZeroDivisionError):
        pass
    
p = int(f * 100)
if p <= 1:
    print("E")
elif p >= 99:
    print("F")
else:
    print(f"{p}%")

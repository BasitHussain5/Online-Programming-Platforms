grocery = {}

while True:
    try:
        i = input().lower()
        if i in grocery:
            grocery[i] += 1
        else:
            grocery[i] = 1
    except EOFError:
        for key in sorted(grocery.keys()):
            print(grocery[key], key.upper())
            
        break

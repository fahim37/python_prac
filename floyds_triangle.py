def triangle():
    row = 4
    count = 1
    for i in range(0, row):
        for j in range(0, i+1):
            print(f"{count}",end="")
            count += 1
        print()
triangle()
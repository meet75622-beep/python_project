print("Sara's Pattern and Numbers")

while True:
    print("\nSelect: 1.Pattern 2.Numbers 3.Exit")
    ans = input("Choice: ")

    if ans == "1":
        rw = int(input("Rows: "))
        if rw <= 0:
            print("break used, rows must be >0")
            break
        for a in range(1, rw+1):
            for b in range(a):
                print("*", end="")
            print()
    elif ans == "2":
        sss = int(input("Start: "))
        eee = int(input("End: "))
        if sss >= eee:
            print("continue to menu")
            continue
        ssum = 0
        for z in range(sss, eee+1):
            if z % 2 == 0:
                print(z, "is EVEN")
            else:
                print(z, "is ODD")
            ssum += z
        print("Sum is", ssum)
    elif ans == "3":
        print("Exit done.")
        break
    else:
        print("Error input")

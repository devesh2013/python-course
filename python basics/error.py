valid = False
while not valid:
    try:
        n = int(input("enter a number:"))
        while n % 2 == 0:
            print("bye")
            n = int(input("enter a n.o:  "))
        valid = True
    except ValueError:
        print("invalid")


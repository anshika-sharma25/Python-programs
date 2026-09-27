n = int(input("Enter a number: "))

if n <= 1:
    print("Not a Prime Number")
else:
    prime = True

    for i in range(2, n):
        if n % i == 0:
            prime = False
            break

    if prime:
        print("Prime Number")
    else:
        print("Not a Prime Number")
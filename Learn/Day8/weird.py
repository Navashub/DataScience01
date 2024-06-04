n = int(input('Enter the number: '))

if n % 2 != 0:
    print("Weird")
else:
    if 2 <= n <= 5:
        print("Not weird")
    elif 6 <= n <= 20:
        print("Weird")
    elif n >20:
        print("Not werid")


a=int(input("Enter the number of rows you want: "))
b=1
for i in range(a):
    for j in range(b):
        print("*", end=" ")
    print("\n")
    b=b+1
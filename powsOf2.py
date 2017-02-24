#prints n powers of 2

def main(n):
    arr = []
    for i in range(n):
        arr.append(i**2)
    print(arr)

main(7)
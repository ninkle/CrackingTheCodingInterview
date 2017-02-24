def main(str):
    lis = []
    for i in str:
        lis.append(i)

    lis = sorted(lis)

    for i in range(len(lis)-1):
        if lis[i] == lis[i+1]:
            print("There are repeat characters here.")
            return

    print("All characters are unique.")
    return

\

main("Fitzgeralde")


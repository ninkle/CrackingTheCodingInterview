def main(str1, str2):

    if len(str1) != len(str2):
        print("Not a permutation!")
        return
    else:
        lis1 = []
        lis2 = []
        for i in str1:
            lis1.append(i)
        for i in str2:
            lis2.append(i)

    if sorted(lis1) == sorted(lis2):
        print("These are permutations")
        return
    else:
        print("Not a permutation!")
        return

main("nicoee", "nicole")
